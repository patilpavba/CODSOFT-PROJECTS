
def chatbot():
    print(" Hello! I'm ChatBuddy. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("ChatBuddy: Hey there! do you want any help?")
        
        elif 'All well?' in user_input:
            print("ChatBuddy: I am great, thanks for asking")
        
        elif 'your name' in user_input:
            print("ChatBuddy: i am chatbuddy made by by simple python programing")
        
        elif 'suggest 3 things to stay positive' in user_input:
            print("ChatBuddy: Be grateful,listen good music,be calm!")
        
        elif 'bye' in user_input:
            print("ChatBuddy:  Good Bye! Talk to you later.")
            break
        
        else:
            print("ChatBuddy: Hmm... I didn't get that. Can you try saying it differently?")

chatbot()

