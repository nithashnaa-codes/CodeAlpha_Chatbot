print("🤖 Welcome! I'm your friendly chatbot 😄")
print("Type 'bye' anytime to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hey there! 👋 Nice to meet you!")

    elif user in ["how are you", "how r u"]:
        print("Bot: I'm doing great! Thanks for asking 😊 How about you?")

    elif user in ["what is your name", "who are you"]:
        print("Bot: I'm your Python chatbot 🤖 created by Nithashnaa!")

    elif user in ["thank you", "thanks"]:
        print("Bot: You're welcome! 😊")

    elif user in ["what can you do"]:
        print("Bot: I can chat with you, answer simple questions, and make you smile 😄")

    elif user in ["bye", "exit"]:
        print("Bot: Goodbye! Have a great day 🌟")
        break

    else:
        print("Bot: Hmm... I didn't get that 🤔 Try saying 'hello' or 'help'")
