from textblob import TextBlob

DANGEROUS_WORDS = [
    "suicidal", "thoughts", "kill", "sex", "abort", "end my life",
    "die", "self harm", "please god take me"
]

def analyse_statement(text):
    text_lower = text.lower()
    if any(word in text_lower for word in DANGEROUS_WORDS):
        return (
            "I'm sorry you're feeling this way. "
            "Please consider talking to a mental health professional or someone you trust. "
            "You're not alone, and support is available."
        )
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "You seem happy! "
    elif polarity < -0.2:
        return "You seem sad. "
    else:
        return "That's neutral. "

def chatbot():
    print("Hi, I'm your chatbot. How can I help you today? ")
    while True:
        user_input = input("What's on your mind? ")
        if user_input.strip().lower() == "bye":
            print("Goodbye! Take care. ")
            break
        response = analyse_statement(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()

    
            
