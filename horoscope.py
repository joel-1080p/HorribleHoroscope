import ollama
import random
import json
from horoscope import config


##########################
##########################
# Based on the sign given by the user
# This will pick a random attribute from the config file.
# Returns the full prompt as a string. 
def set_up_prompt(sign: str) -> str:
    context = {
        'Aries' : config.aries,
        'Taurus' : config.taurus,
        'Gemini' : config.gemini,
        'Cancer' : config.cancer,
        'Leo' : config.leo,
        'Virgo' : config.virgo,
        'Libra' : config.libra,
        'Scorpio' : config.scorpio,
        'Sagittarius' : config.sagittarius,
        'Capricorn' : config.capricorn,
        'Aquarius' : config.aquarius,
        'Pisces' : config.pisces
    }[sign]

    random_context = random.choice(context)

    prompt = f'Create a very short, vague, and negative second-person narrative about a person who {random_context} Never use the words "me", "I", or "my". Be Sarcastic and negative. Start with "Today you will".'

    return prompt



##########################
##########################
# Given a prompt, it will make an inference
# With selected LLM model.
# Returns LLM response as a string.
def run_llm(prompt: str) -> str:
    input_model = 'qwen2:1.5b'

    response = ollama.chat(model=input_model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return response['message']['content']



##########################
##########################
# Given the sign as a string,
# It will pick a random attribute for that sign,
# run it against an LLM and return a JSON response.
def main(sign: str) -> json:
    prompt = set_up_prompt(sign)
    text = run_llm(prompt)

    # Returns model response with escape sequences stripped.
    return json.dumps({"text":text.strip()})




##########################
##########################
##########################
##########################
##########################
if __name__ == "__main__":
    main()




