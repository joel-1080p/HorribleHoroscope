# Horrible Horoscope


Horrible Horoscope tells you about your day with the aspect of the negatives of your sign.

## RUNNING PI SEARCH
- Download [Ollama](https://ollama.com/download) to easly run an LLM to infrence from.
- Open Terminal or CMD and type `ollama run qwen2:1.5b` to download the model.
- You can use any model, this is just mainly for speed purposes.
  
## HOW IT WORKS
- `horoscope.py` uses the `config.py` to pull a random attribute from the sign chosen.
- This attriibute will be added to the prompt being fed into the model.
- EXAMPLE : The script chose this for a Leo 'can come across as overly proud and boastful, believing they are superior to others.'
- The full prompt will then be `Create a very short, vague, and negative second-person narrative about a person who can come across as overly proud and boastful, believing they are superior to others. Never use the words "me", "I", or "my". Be Sarcastic and negative. Start with "Today you will"`
- The model will then create the horoscope to be displayed.

## HOW I USE IT
- I use it in my portfolio website as part of the react/flask backend. [Website](http://38.125.229.163:3000/horrible-horoscope)

## Requirements

-   [Python](https://www.python.org) \>= 2.7, 3.4+
-   [Flask](https://flask.palletsprojects.com/en/3.0.x/) \>= 3.0.3

### P.S.

Please drop me a note with any feedback you have.

**Joel**
