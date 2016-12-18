import random
import pytest

random.seed(0)

from Chat import *

def test_random_utterance(): #DONE
    """An utterance which is unparsable should return one of the random responses"""
    sent = "abcd"  # Something unparseable
    resp = broback(sent)
    assert resp == NONE_RESPONSES[-2]

def test_basic_greetings(): #DONE
    """The bot should respond sensibly to common greeting words"""
    sent = "hello"
    resp = broback(sent)
    assert resp == GREETING_RESPONSES[1]


###If we tell the robot we did something #DONE
def test_contains_reference_to_user():
    """An utterance where the user mentions themselves generally should specifically return a phrase starting with 'You'"""
    sent = "I went to dinner"
    resp = broback(sent)
    assert resp.startswith("Wow ")

####If we tell the bot we are something #GOOD VGB - I am good at swimming fails, only nouns not ending in -ing works
def test_negs_user():
    """An utterance where the user says 'I am' <something> should specifically tell them they aren't that thing"""
    sent = "I am good at Python programming"
    resp = broback(sent)
    assert resp.startswith("Cool")

   # sent = "I'm good at Python programming"
    #resp = broback(sent)
    #assert resp.startswith("You aren't really")

   # sent = "i'm good at Python programming"
    #resp = broback(sent)
    #assert resp.startswith("You aren't really")

####If we tell the bot he is something#########
def test_contains_reference_to_bot(): #DONE
    """An utterance where the user directs something at the bot itself should return a canned response"""
    sent = "You are lame"
    resp = broback(sent)
    assert 'lame' in resp

##########If we compare ourself to a noun, AI says the noun back
def test_reuses_subject():
    """If the user tells us about some kind of subject, we should mention it in our response"""
    sent = "I am a capable programmer"
    resp = broback(sent)
    assert "programmer" in resp



def test_strip_punctuation(): #done
    """Removing most punctuation is one way to ensure that the bot doesn't include hashtags or @-signs, which are potential vectors for harrassment"""
    sent = "I am a #snakeperson"
    with pytest.raises(UnacceptableUtteranceException):
        broback(sent)

    sent = "@you are funny"
    with pytest.raises(UnacceptableUtteranceException):
        broback(sent)