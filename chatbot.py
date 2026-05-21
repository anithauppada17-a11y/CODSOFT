import random

print("ChatBot: Hello! Type 'bye' to exit.")

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine!", "Doing great!", "Awesome!"],
    "what is your name": ["I'm a chatbot created using Python."],
    "help": ["I can help you chat."],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

while True:
    user_input = input("You: ").lower()

    found = False

    for key in responses:
        if key in user_input:
            print("ChatBot:", random.choice(responses[key]))
            found = True

            if key == "bye":
                exit()

    if not found:
        print("ChatBot: Sorry, I don't understand that.")