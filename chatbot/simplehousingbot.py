import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Store locally to prevent accidental key publication
openai.api_key = os.getenv('API_KEY')

# This is a simple bot that can give you information related to California housing prices
def ask_openai(question):
    csv_file_path = 'california_housing_train.csv'
    with open(csv_file_path, 'r') as file:
      csv_text = file.read()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that is knowledgeable of California housing data, given here: " + csv_text},
            {"role": "user", "content": question}
        ]
    )
    answer = response['choices'][0]['message']['content']
    return answer

print("Welcome, this is a California housing chat bot. Have any questions? Type 'Goodbye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'goodbye':
        break
    print("AI: ", ask_openai(user_input))