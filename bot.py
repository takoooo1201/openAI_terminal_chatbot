import os
from dotenv import load_dotenv
from openai import OpenAI  # Assuming OpenAI is your imported client

# Load the .env file
load_dotenv()

# Get the API key from the environment variable
key = os.getenv("key")

# Initialize the OpenAI client
client = OpenAI(api_key=key)



def chat_with_gpt4o():
    #print("Chat with GPT-4o! Type 'exit' to end the conversation.\n")
    

    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        print("-----")
        user_input = input("")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        conversation_history.append({"role": "user", "content": user_input})

        try:
            # Request a response from GPT-4o
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=conversation_history
            )

            assistant_message = completion.choices[0].message.content
            conversation_history.append({"role": "assistant", "content": assistant_message})
            print("-----")
            print(f"{assistant_message}\n")

        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    chat_with_gpt4o()

