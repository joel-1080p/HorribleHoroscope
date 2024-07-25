import ollama
import random
import json
from horoscope import config


##########################
##########################
#
def set_up_prompt(sign):
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

    prompt = f'Create a very short, vague, and negative second-person narrative about a person who {random_context}. Never use the words "me", "I", or "my". Be Sarcastic and negative. Start with "Today you will".'

    return prompt



##########################
##########################
#
def run_model_and_print(prompt):
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
#
def main(sign: str):
    prompt = set_up_prompt(sign)
    text = run_model_and_print(prompt)
    return json.dumps({"text":text.strip()})




##########################
##########################
##########################
##########################
##########################
if __name__ == "__main__":
    main()




