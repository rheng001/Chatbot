
---------
UCR CS-170 Artificial Intelligence  Final Project
------------

------
Chatbot Menu
--------

***I am now continuing the work of Chatbot, alone and any further changes is done personally by me, Richard Heng***


![Chat Menu](http://i.imgur.com/QRoJoYn.png)


----------
High Level Description
-----

Our project is a simple AI that chats with the user and makes responses based on the conservation. Our main goal for the AI is to have it analyze the conversation and adapt to it so it may respond appropriately. For example, based on the user’s speech, the AI will shift itself toward a personality, such as Good, if the user is friendly, and Hostile, if the user is unfriendly.

------
User Guide
---

Must have a directory/folder containing the following files:

	Chat.pyi

	Chat_memory.py

	Chat_test.py

	ChatBotGUI.py

	negative.txt

	positive.txt

Using Python 3

Install the following python modules: pip install 

	requests

	tweepy

	textblob

	textblob.download_corpora

	pytest

After installing the following using any Python IDE or whatever you use to operate python and run the python file ChatBotGUI to start the program.

-----
Source Files
-----

*   **Chat.py**

    * Contains main program functions.

*   **Chat_memory.py**

    * Contains a database of Chatbot memory.

*   **Chat_test.py**

    * Contains Chatbot test case code.

*   **ChatBotGUI.py**
   
    * Contains the main program and gui code.

*   **negative.txt**

    * Contains a list of negative words.

*   **positive.txt**

    * Contains a list of positive words.

-----
Functions and Test Cases
-----

The following sentence structures are supported:

*	What time is it?
*	Who am I
*	Who are you


*	Testing we are something
	*	I am good at ____ 

*	Testing reference to bot
	*	You are ___

*	Asking if bot knows about something
	*	Have you heard of a ___  
    
-----
Bugs and Limitations
-----

Capitalization matters

Some phrasess the chatbot will not understand

Unable to handle certain user responses and will crash

------
Citations
---

Source code used and inspired by Liza Daly's Brobot from https://github.com/lizadaly/brobot
