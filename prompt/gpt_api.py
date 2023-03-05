import openai
import re

from prompt.pre_process import clean_text

# Set up OpenAI API credentials
openai.api_key = ""

# Define the function to generate questions from text
def generate_questions(text):
    # Clean up the text by removing line breaks and extra whitespace
    text = clean_text(text)
    # Set up the prompt for the GPT-3 API
    prompt = (f"Generate historical context questions from:\n\n{text}\n\n")
            #   "1. Who are some notable football players mentioned in the text?\n"
            #   "2. What is the significance of Lionel Messi's performance in the match mentioned in the text?\n"
            #   "3. How has Lionel Messi performed for PSG and for his national team this season?\n"
            #   "4. What impact did Lionel Messi have on his former team, Barcelona?\n"
            #   "5. Who were the members of the MSN attacking trio at Barcelona, and what were their accomplishments?\n"
            #   "6. How did Neymar's departure from Barcelona affect the team's performance?\n"
            #   "7. What is the significance of the Golden Boot award, and how did Luis Suarez win it in 2015-16?\n"
            #   "8. How has Messi's legacy as a football player evolved over time?\n"
            #   "9. What are some of the reasons that Messi is considered by many to be one of the greatest football players of all time?\n"
            #   "10. How has football evolved over time, and what role have players like Messi played in shaping the sport's history?\n")

    # Set up the GPT-3 API request
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        n = 1,
        stop=None
    )

    # Extract the generated questions from the API response
    generated_questions = response.choices[0].text.strip()

    # Split the generated questions into a list and return it
    return generated_questions.split('\n')
# Call the function with some sample text

