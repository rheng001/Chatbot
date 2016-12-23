from __future__ import print_function, unicode_literals
import random
import logging
import time

from textblob import TextBlob
from Chat_memory import *

############GLOBALS##################
#global personality
personality = 50
i = 0

#######this loads the sentiment analysis words into ai memory#########
with open("positive.txt",'r') as f:
    data = f.read().replace(",",'')
    pos = [s.strip() for s in data.split(' ') if s]

with open("negative.txt", 'r') as g:
    data2 = g.read().replace(",", '')
    neg = [t.strip() for t in data2.split(' ') if t]

##############################################################

#######Generates User logs for maintence##############
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#######################################################
def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""

    greeting = any(substring in sentence.lower() for substring in GREETING_KEYWORDS)

    global personality

    if greeting == True and personality >= 45 and personality <= 55:
        return random.choice(GREETING_RESPONSES)

    if greeting == True and personality > 55:
        return random.choice(POS_GREETING_RESPONSE) + " " + random.choice(POS_END)

    if greeting == True and personality < 45:
        return random.choice(NEG_GREETING_RESPONSE) + " " + random.choice(NEG_END2)

############################### end #######################################


# If the user tries to tell us something about ourselves, use one of these responses
COMMENTS_ABOUT_SELF = [
    "You're just jealous",
    "I worked really hard on that",
    "My Klout score is {}".format(random.randint(100, 500)),
]
# end



def starts_with_vowel(word):
    """Check for pronoun compability -- 'a' vs. 'an'"""
    return True if word[0] in 'aeiou' else False

###main loop
def broback(sentence):
    """Main program loop: select a response for the input sentence and return it"""
    resp = respond(sentence)
    logger.info("CHATBOT: respond to %s", sentence)
    return resp


# start:example-pronoun.py
def find_pronoun(sent): ### personal pronoun is a pronoun that is associated primarily with a particular person
    """Given a sentence, find a preferred pronoun to respond with. Returns None if no candidate
    pronoun is found in the input"""
    pronoun = None

    for word, part_of_speech in sent.pos_tags:
        # Disambiguate pronouns
        if part_of_speech == 'PRP' and word.lower() == 'you': #I hate you
            pronoun = 'I'
        elif part_of_speech == 'PRP' and word == 'I':
            ######## If the user mentioned themselves, then they will definitely be the pronoun###
            ####User says they did something/bot responds################
            pronoun = 'You' ###No Way
    return pronoun
# end

def find_verb(sent):
    """Pick a candidate verb for the sentence."""
    verb = None
    pos = None
    for word, part_of_speech in sent.pos_tags:
        if part_of_speech.startswith('VB'):  # This is a verb
            verb = word
            pos = part_of_speech
            break
        #if part_of_speech == 'VBD':
            #verb = word
            #pos = part_of_speech
           #break
    return verb, pos


def find_noun(sent):
    """Given a sentence, find the best candidate noun."""
    noun = None

    if not noun:
        for w, p in sent.pos_tags:
            if p == 'NN':  # This is a noun
                noun = w
                break
    if noun:
        logger.info("Found noun: %s", noun)

    return noun

def find_pnoun(sent):
    """Given a sentence, find the best candidate possessive noun"""

    pnoun = None

    if not pnoun:
        for w, p in sent.pos_tags:
            if p == 'PRP$':
                pnoun = w
                break
    if pnoun:
        logger.info("Found possessive noun: %s", pnoun)

    return pnoun

def find_prnoun(sent):

    prnoun = None

    if not prnoun:
        for w, p in sent.pos_tags:
            if p == 'NNP':
                prnoun = w
                break
    if prnoun:
        logger.info("Found proper noun: %s", prnoun)

    return prnoun

def find_adjective(sent):
    """Given a sentence, find the best candidate adjective."""
    adjective = None

    if not adjective:
        for w, p in sent.pos_tags:
            if p == 'JJ':  # This is an adjective
                adjective = w
                break
    return adjective



# start:example-construct-response.py
def construct_response(pronoun, noun, pnoun, verb, adjective): #NO case match
    """No special cases matched, so we're going to try to construct a full sentence that uses as much
    of the user's input as possible"""
    resp = []

    #if pronoun:
        #resp.append(pronoun)

    # We always respond in the present tense, and the pronoun will always either be a passthrough
    # from the user, or 'you' or 'I', in which case we might need to change the tense for some
    # irregular verbs.



    if verb:
        verb_word = verb[0]
        if verb_word in ('be', 'am', 'is', "'m"):  # This would be an excellent place to use lemmas!
            if pronoun.lower() == 'you' and personality >= 55:  ######## work in progress
                resp.append("Thats great to hear")
                resp.append(noun)
                resp.append("is awesome")
            if pronoun.lower() == 'you' and personality <= 45:
                resp.append("You arent really")
                resp.append(adjective)
                resp.append("at")
                resp.append(noun)
            if pronoun.lower() == 'you' and personality == 50:
                resp.append("Oh") ##Oh, sweet, etc


        if verb_word in ('went'): ###WORK IN progress #I went to dinner
            if pronoun.lower() == 'you':
                resp.append("No way")
    if noun:
        pronoun = "an" if starts_with_vowel(noun) else "a" ####REPLACE THIS LATER
        #resp.append("Thats awesome me too") ## mess with this




    if personality >= 55:
        resp.append(random.choice(POS_END)) ##friend buddy, pal, etc
    if personality <= 45:
        resp.append(random.choice(NEG_END)) #you idiot, you imbecile, who cares punk
    if personality == 50:
        print(noun)
        resp.append("Thats awesome")
        resp.append(noun)
        resp.append("is cool!")
    #else:
        #resp.append(random.choice(("bro", "lol", "bruh", "smh", ""))) ######Response at the end of bot speech neutral

    return " ".join(resp)
# end


# start:example-check-for-self.py
def check_for_comment_about_bot(pronoun, noun, adjective):
    """Check if the user's input was about the bot itself, in which case try to fashion a response
    that feels right based on their input. Returns the new best sentence, or None."""
    resp = None
    if pronoun == 'I' and (noun or adjective):
        if noun:
            #if random.choice((True, False)):
                #resp = random.choice(SELF_VERBS_WITH_NOUN_CAPS_PLURAL).format(**{'noun': noun.pluralize().capitalize()})

            if personality == 45 or personality == 55 or personality == 50:
                resp = random.choice(SELF_VERBS_WITH_NOUN_LOWER).format(**{'noun': noun})
            if personality > 55:
                resp = random.choice(POS_SELF_VERBS_WITH_NOUN_LOWER).format(**{'noun': noun})
            if personality < 45:
                resp = random.choice(NEG_SELF_VERBS_WITH_NOUN_LOWER).format(**{'noun': noun})
        if noun == None:
            if personality == 45 or personality == 55 or personality == 50:
                resp = random.choice(SELF_VERBS_WITH_ADJECTIVE).format(**{'adjective': adjective})
            if personality > 55:
                resp = random.choice(POS_SELF_VERBS_WITH_ADJECTIVE).format(**{'adjective': adjective})
            if personality < 45:
                resp = random.choice(NEG_SELF_VERBS_WITH_ADJECTIVE).format(**{'adjective': adjective})
           # resp = random.choice(SELF_VERBS_WITH_ADJECTIVE).format(**{'adjective': adjective})
    return resp

def check_for_name(pnoun, noun, prnoun, adjective):

    resp = None

    if (pnoun == 'my' or pnoun == 'My') and noun == 'name' and not prnoun:
        resp = 'Oh hello ' + adjective

    elif (pnoun == 'my' or pnoun == 'My') and noun == 'name' and not adjective:
        resp = "Oh hello " + prnoun

    return resp




###FIX CAPITALIZATION ERRORS
def preprocess_text(sentence):
    """Handle some weird edge cases in parsing, like 'i' needing to be capitalized
    to be correctly identified as a pronoun"""
    cleaned = []
    words = sentence.split(' ')
    for w in words:
        if w == 'i':
            w = 'I'
        if w == "i'm":
            w = "I'm"
        if w == 'im' or w == 'Im':
            w = "I'm"
        if w == 'your':
            w = 'you are'
        cleaned.append(w)

    return ' '.join(cleaned)

# start:example-respond.py
def respond(sentence):
    """Parse the user's inbound sentence and find candidate terms that make up a best-fit response"""
    cleaned = preprocess_text(sentence)
    parsed = TextBlob(cleaned)

    # Loop through all the sentences, if more than one. This will help extract the most relevant
    # response text even across multiple sentences (for example if there was no obvious direct noun
    # in one sentence
    pronoun, noun, pnoun, prnoun, adjective, verb = find_candidate_parts_of_speech(parsed)

    # If we said something about the bot and used some kind of direct noun, construct the
    # sentence around that, discarding the other candidates

    if pronoun == 'I':
        resp = check_for_comment_about_bot(pronoun, noun, adjective)
    else:
        resp = check_for_name(pnoun, noun, prnoun, adjective)

    # If we just greeted the bot, we'll use a return greeting
    if not resp:
        resp = check_for_greeting(parsed)

    if not resp:
        # If we didn't override the final sentence, try to construct a new one:
        if not pronoun:
            resp = random.choice(NONE_RESPONSES)
        elif pronoun == 'I' and not verb:
            resp = random.choice(COMMENTS_ABOUT_SELF)
        else:
            resp = construct_response(pronoun, noun, pnoun, prnoun, verb, adjective)

    # If we got through all that with nothing, use a random response
    if not resp:
        resp = random.choice(NONE_RESPONSES)

    logger.info("Returning phrase '%s'", resp)
    # Check that we're not going to say anything obviously offensive
    #filter_response(resp) ##########This checks for negative words

    return resp

def find_candidate_parts_of_speech(parsed):
    """Given a parsed input, find the best pronoun, direct noun, adjective, and verb to match their input.
    Returns a tuple of pronoun, noun, adjective, verb any of which may be None if there was no good match"""
    pronoun = None
    noun = None
    pnoun = None
    prnoun = None
    adjective = None
    verb = None
    for sent in parsed.sentences:
        pronoun = find_pronoun(sent)
        noun = find_noun(sent)
        pnoun = find_pnoun(sent)
        prnoun = find_prnoun(sent)
        adjective = find_adjective(sent)
        verb = find_verb(sent)
    logger.info("Pronoun=%s, noun=%s, pnoun=%s, prnoun=%s, adjective=%s, verb=%s", pronoun, noun, pnoun, prnoun, adjective, verb)
    return pronoun, noun, pnoun, prnoun, adjective, verb

def getUniqueNest(iterable):
    seen = set()
    for item in iterable:
        if item[0] not in seen:
            seen.add(item[0])
            yield item


################FEATURE NOT FULLY IMPLEMENTED#########################
def What_is(saying):
    if 'What is an' in saying or 'what is an' in saying:
        if 'a' in saying: ##If a used first, 2nd term will be whole sentence
            saying.replace('a', 'b')
            #print(saying)
            tokenized = saying.split('What is an ')

        if 'an' in saying: ##An must be first or 2nd term will read all of them?
            tokenized = saying.split('What is an ')

    if 'Chatbot' in saying or 'chatbot,' in saying: ## input word is a
        if 'an' in saying:
            tokenized = saying.rsplit('an ', 1)[1]
            print("Ill learn") #### DONE

    word = tokenized
    word = [i for i in word if i != '']
    from Chat_memory import MEMORY

    if word not in MEMORY:
        word = ''.join(word)
        print("I dont know what an", word, "is.")

        global i
        if len(MEMORY[i]) != 2:
            MEMORY[i].append(word)

            '''
            for item in MEMORY:
                if word in item:
                    print('found', word, 'in', MEMORY)
                    MEMORY.remove(-1)
                    print(MEMORY)'''

            if len(MEMORY[i]) == 2: #(2 words in element)

                i += 1
    else:
        print(word, "already in memory")


    for sublist in MEMORY:
        if sublist in MEMORY:
            if word in sublist:
               print("A", word, "is a", sublist[-1]) #prints out twice'''

    print(MEMORY)

##############################################################

###############MAIN########################
Welcome = "Welcome to the CS 170 Chatbot AI Program!" '\n' "You can start talking to the AI. Type 'end' to exit the program" '\n'
print(Welcome)

########LEARNING TO BE IMPLEMENTED LATER#############
'''
saying = ""

while saying != "end" or saying != "quit" or saying != "exit":

    saying = input("You: ")

    elif "What is an" not in saying and 'what is an' not in saying and 'chatbot' not in saying:
       print(broback(saying))

    else:
        What_is(saying)'''

