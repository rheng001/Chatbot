from tkinter import *
from Chat import *
import Chat
BAD = ['bitch', 'cunt', 'asshole']
GOOD = ['awesome', 'pretty', 'kind','generous']

###########MAIN INITIALIZATION###################
Chat.personality = 50
root = Tk() #global blank window
Text_widget = Text(root, bd=7,font = ('Courier New Bold', '10'),fg='black',bg='snow')
Text_widget.tag_configure("mytag4", justify=CENTER)
Text_widget.insert(END,'Welcome to CS 170 ChatBot AI \n \n',"mytag4")
Text_widget.insert(END,'Instructions: Press enter to send message in the text box \n \n')
Entry_widget = Entry(root, width=108, bg='snow',fg = 'black')

user_input=""
def main():
    root.title('ChatBot')
    root.geometry("700x850")
    root.configure(bg = 'dodger blue')


def textbox():
    label1 = Label(root, text="Welcome to the CS 170 Chatbot AI Program!", fg = 'white', bg = 'dodger blue',
                   font = ('Courier New Bold', '16'))
    label1.grid(row = 0)
    Text_widget.grid(column = 0)
    scrollbar = Scrollbar(root,command =Text_widget.yview())
    scrollbar.grid(row = 1, column = 1 , rowspan = 2, sticky = N+S+W)
    Text_widget['yscrollcommand'] = scrollbar.set
    Entry_widget.grid()
    # from here http://stackoverflow.com/questions/13832720/how-to-attach-a-scrollbar-to-a-text-widget

def clearscreen():
    Text_widget.delete(1.0, END)
    Text_widget.tag_configure("mytag4", justify=CENTER)
    Text_widget.insert(END, 'Welcome to CS 170 ChatBot AI \n \n', "mytag4")
    Text_widget.insert(END, 'Instructions: Press enter to send message in the text box \n \n')

# display user input into text box
def getTextInput(str):  #####RObot

    Text_widget.tag_configure("mytag3", background='lawn green')
    Text_widget.insert(END, str, "mytag3")
    Text_widget.insert(END, "\n")
    Text_widget.insert(END, "\n")
    Text_widget.yview_pickplace(END)  #Auto scroll to the end of the text
    #mystring = Text_widget.get('1.0', 'end-1c')
    #print mystring
    # http://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-box-widget


def sendTextOutput(str):
    #Chatbot_string =  str + ' -Chatbot '
    output_string = str
    Chat_string = ' Chatbot: ' +output_string
    # this switches text to other side
    Text_widget.tag_configure("mytag2", justify='right')
    Text_widget.insert(END, ' ', "mytag2")
    Text_widget.tag_configure("mytag1", justify = 'right', background ='turquoise1')
    Text_widget.insert(END,Chat_string,"mytag1")
    Text_widget.insert(END, "\n")
    Text_widget.insert(END, "\n")
    Text_widget.yview_pickplace(END) #Auto scroll to the end of the text



def clear_button():
    button2 = Button(root, text="Clear Screen", bg='white', fg='dodger blue', command=clearscreen, width = 32,font =
    ('Courier New Bold', '12'))
    button2.grid()

## get input from user
## must send to AI
def enterclick(event):
    Entry_widget.grid()

    saying =""
    while saying != "end" or saying != "quit" or saying != "exit":
        saying = Entry_widget.get()
        user_input = 'User: ' + Entry_widget.get()
        getTextInput(user_input)
        Entry_widget.delete('0', 'end')
        posWord = any(substring in saying for substring in pos)
        negWord = any(substring in saying for substring in neg)
        if posWord == True:
            Chat.personality += 5
            displayLabelPercentage()
        if negWord == True:
            Chat.personality -= 5
            displayLabelPercentage()

        if saying == 'end' or saying == 'quit' or saying == 'exit':
            sendTextOutput("Goodbye")
            break

        elif 'time' in saying:
            Time = "It is " + time.strftime('%I:%M %p %Z on %b %d, %Y')
            sendTextOutput(Time)

        elif 'name' in saying:
            sendTextOutput("My name is Chatbot")

        elif 'Who are you' in saying or 'Who am I' in saying:
            if 'Who am I' in saying:
                if Chat.personality == 45 or Chat.personality == 55 or Chat.personality == 50:
                    sendTextOutput("You are a CS 170 Student")
                if Chat.personality > 55:
                    sendTextOutput("A " + Chat.random.choice(POS_END))
                if Chat.personality < 45:
                    sendTextOutput("A " + Chat.random.choice(NEG_END2))
            if 'Who are you' in saying:
                sendTextOutput("I am a CS 170 Chatbot AI")

        elif "What is an" not in saying and 'what is an' not in saying and 'chatbot' not in saying:
            sendTextOutput(Chat.broback(saying))

        if 'What' in saying or 'what' in saying:
            sendTextOutput(Chat.What_is(saying))


        break;  # it wont read other enter click unless its outside

## reads enter button
## calls method enter click
Entry_widget.bind("<Return>",enterclick)
Entry_widget.pack

def createLabelPercentage():
    empty = Label(root, fg = 'white', bg = 'dodger blue')
    empty.grid(row = 5)
    percentage_label = Label(root, text="Personality Level ", fg='white', bg ='dodger blue',font =
    ('Courier New Bold','14'))
    percentage_label.grid(row=6)
def displayLabelPercentage():
    percentage_label_display = Label(root, text=Chat.personality, fg='white', bg ='dodger blue',font =
    ('Courier New Bold','14'))
    percentage_label_display.grid(row=7)

def displayGoodPercentage():
    Chat.personality = 70
    percentage_label_display = Label(root, text=Chat.personality, fg='white', bg ='dodger blue',font =
    ('Courier New Bold','14'))
    percentage_label_display.grid(row=7)
def displayBadPercentage():
    Chat.personality = 30
    percentage_label_display = Label(root, text=Chat.personality, fg='white', bg ='dodger blue',font =
    ('Courier New Bold','14'))
    percentage_label_display.grid(row=7)


def displayNeutralPercentage():
    Chat.personality = 50
    percentage_label_display = Label(root, text=Chat.personality, fg='white', bg ='dodger blue',font =
    ('Courier New Bold','14'))
    percentage_label_display.grid(row=7)


def goodButton():

    button3 = Button(root, text="Good", bg='white', fg='dodger blue',command = displayGoodPercentage, width=32, font=
    ('Courier New Bold', '12'))
    button3.grid()

def neutralButton():

    button4 = Button(root, text="Neutral", bg='white', fg='dodger blue', command = displayNeutralPercentage,width=32, font=
    ('Courier New Bold', '12'))
    button4.grid()

def badButton():
    button5 = Button(root, text="Bad", bg='white', fg='dodger blue', command = displayBadPercentage,width=32, font=
    ('Courier New Bold', '12'))
    button5.grid()


if __name__ == '__main__':
    main()
    textbox()
   # inputbox()  # might not need it just write on text box
    clear_button()
    createLabelPercentage()
    displayLabelPercentage()
    goodButton()
    neutralButton()
    badButton()
    root.mainloop()