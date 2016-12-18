#This is the storage file

FILTERWORDS = []

#List of possible greeting wards
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "What's up", "hey", "whats up")

#List of words AI can respond back with
GREETING_RESPONSES = ["Hello", "Hi", "What's up", "Sup", "How's it going"]
NEG_GREETING_RESPONSE = ["What do you want", "Okay...", "Umm hi", "Whatever"]
POS_GREETING_RESPONSE = ["Hiya!","Howdy", "Yo!", "Greetings!" ]

POS_END = ["friend", "buddy", "pal"]
NEG_END = ["you idiot", "you moron", "human"]
NEG_END2 = ["idiot", "moron", "stupid human"]

SELF_VERBS_WITH_NOUN_CAPS_PLURAL = [
    "My last startup totally crushed the {noun} vertical",
    "Were you aware I was a serial entrepreneur in the {noun} sector?",
    "My startup is Uber for {noun}",
    "I really consider myself an expert on {noun}",
]

###Telling AI they are something "You are....
SELF_VERBS_WITH_NOUN_LOWER = [
    "Yeah I know all about {noun}s",
    "What do you want to know about {noun}s",
]

POS_SELF_VERBS_WITH_NOUN_LOWER = ["Yep!, I sure do know about {noun}s", "I do!, want to hear more about {noun}?",
                                  "I think {noun}s are really interesting!"]

NEG_SELF_VERBS_WITH_NOUN_LOWER = ["Of course I know about {noun}s, you don't?",
                                  "You wouldn't understand things about {noun}s",
                                  "I don't think you're able to understand {noun}s like I do"]

###########Telling the bot he is something##################
SELF_VERBS_WITH_ADJECTIVE = [
    "I'm personally building the {adjective} Economy",
    "I consider myself to be a {adjective}preneur",
]
NEG_SELF_VERBS_WITH_ADJECTIVE = ["Well you're {adjective} as well", "I know you're {adjective} but what am I?", "You're {adjective} too"]

POS_SELF_VERBS_WITH_ADJECTIVE = ["Thanks, you're {adjective} as well!", "I appreciate you calling me {adjective}", "Aww! Your're {adjective} too"]
# end


# Sentences we'll respond with if we have no idea what the user just said
NONE_RESPONSES = [ "Are you alright?",
                    "Anyone there?",
                    "Umm what?" ]

MEMORY = [[] for _ in range(20)]

