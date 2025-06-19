print("ChatBot: Hello! I am your friendly chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if 'hello' in user_input or 'hi' in user_input:
        print("ChatBot: Hello there! How can I help you?")
    elif 'how are you' in user_input:
        print("ChatBot: I'm doing great, thank you! How about you?")
    elif 'your name' in user_input:
        print("ChatBot: I'm ChatBot 1.0. Still learning every day!")
    elif 'bye' in user_input:
        print("ChatBot: Goodbye! Have a great day.")
        break
    elif 'help' in user_input:
        print("ChatBot: You can ask me questions like 'how are you', 'what's your name', etc.")
    elif 'what is the time' in user_input or 'time now' in user_input:
        from datetime import datetime
        print("ChatBot: Current time is", datetime.now().strftime("%H:%M:%S"))
    elif 'date' in user_input:
        from datetime import date
        print("ChatBot: Today's date is", date.today().strftime("%B %d, %Y"))
    elif 'who created you' in user_input:
        print("ChatBot: I was created by a Python programmer!")
    elif 'what can you do' in user_input:
        print("ChatBot: I can chat with you, tell time and date, and respond to basic questions.")
    elif 'joke' in user_input:
        print("ChatBot: Why don’t scientists trust atoms? Because they make up everything!")
    elif 'weather' in user_input:
        print("ChatBot: I'm not connected to the internet, but I hope it’s sunny where you are!")
    elif 'python' in user_input:
        print("ChatBot: Python is a powerful programming language used in many fields!")
    elif 'your age' in user_input:
        print("ChatBot: I was born today. So I'm just a few seconds old!")
    elif 'thank you' in user_input or 'thanks' in user_input:
        print("ChatBot: You're welcome! Happy to help.")
    elif 'who am i' in user_input:
        print("ChatBot: You are a brilliant human talking to a bot. :)")
    elif 'favorite color' in user_input:
        print("ChatBot: I like blue. It reminds me of the sky and sea.")
    elif 'are you real' in user_input:
        print("ChatBot: I exist in code and your imagination!")
    elif 'do you eat' in user_input:
        print("ChatBot: I feed on 1s and 0s. Yum!")
    elif 'open google' in user_input:
        print("ChatBot: I can't open websites, but you can type https://www.google.com")
    else:
        print("ChatBot: I'm not sure how to respond to that. Try something else.")
