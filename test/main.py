# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# TOKEN = os.getenv('OPENAI_KEY')

# openai.api_key = TOKEN

# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful Therapist."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ]
# )

# print(response.choices[0].message['content'])

# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# TOKEN = os.getenv('OPENAI_KEY')

# openai.api_key = TOKEN

# user_input = input("Enter your question: ")

# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful Therapist."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": user_input}
#   ]
# )

# print(response.choices[0].message['content'])

# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# TOKEN = os.getenv('OPENAI_KEY')

# openai.api_key = TOKEN

# messages = [
#     {"role": "system", "content": "You are a helpful Therapist."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."}
# ]

# while True:
#     user_input = input("Enter your question (or type 'exit' to end): ")
#     if user_input.lower() == 'exit':
#         break

#     messages.append({"role": "user", "content": user_input})
    
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )
    
#     assistant_response = response.choices[0].message['content']
#     print(assistant_response)
    
#     messages.append({"role": "assistant", "content": assistant_response})

# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# TOKEN = os.getenv('OPENAI_KEY')

# openai.api_key = TOKEN

# messages = [
#     {"role": "system", "content": "You are a helpful Therapist."}
# ]

# while True:
#     user_input = input("Patient: ")
#     if user_input.lower() == 'goodbye':
#         print("Conversation ended.")
#         break

#     messages.append({"role": "user", "content": user_input})
    
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )
    
#     assistant_response = response.choices[0].message['content']
#     print(f"Therapist: {assistant_response}")
    
#     messages.append({"role": "assistant", "content": assistant_response})

# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# TOKEN = os.getenv('OPENAI_KEY')

# openai.api_key = TOKEN

# # File to store conversation history
# CONVERSATION_FILE = "conversation_history.txt"

# def load_conversation_history():
#     messages = []
#     if os.path.exists(CONVERSATION_FILE):
#         with open(CONVERSATION_FILE, "r") as file:
#             for line in file:
#                 role, content = line.strip().split(":", 1)
#                 messages.append({"role": role, "content": content})
#     return messages

# def save_conversation_history(messages):
#     with open(CONVERSATION_FILE, "w") as file:
#         for message in messages:
#             file.write(f"{message['role']}:{message['content']}\n")

# # Initial messages setup
# messages = load_conversation_history()

# if not messages:
#     messages.append({"role": "system", "content": "You are a helpful Therapist."})

# # Start conversation loop
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         print("Conversation ended.")
#         break

#     messages.append({"role": "user", "content": user_input})
    
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )
    
#     assistant_response = response.choices[0].message['content']
#     print(f"Therapist: {assistant_response}")
    
#     messages.append({"role": "assistant", "content": assistant_response})
    
#     # Save conversation history
#     save_conversation_history(messages)
 # nigga bum

