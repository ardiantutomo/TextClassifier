from classifier import TextClassifier as t

classifier = t.TextClassifier("trained.trn")
state = ""

def callback():
    global state
    if state == "greetings":
        reply = "Hello"
        print (reply)
    elif state == "ask_for_definition":
        # ask for def module
        print("Mantap")
    state = ""

while(True):
    print("Current State: {}".format(state))
    callback()
    user_input = input(">> ")
    state  = classifier.classify(user_input)
