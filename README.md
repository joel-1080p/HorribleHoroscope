# Horrible Horoscope

![IMG_2006 (1)](https://github.com/user-attachments/assets/c7bbf353-4dfb-455a-8742-71768d969a0c)

Horrible Horoscope: Get a hilariously twisted take on your daily horoscope by revealing the snarky, negative side of your sign.

## RUNNING HORRIBLE HOROSCOPE
- Download [Ollama](https://ollama.com/download) to easly run an LLM to infrence from.
- Open Terminal or CMD and type `ollama run qwen2:1.5b` to download the model.
- You can use any model, this is just mainly for speed purposes.
- Make sure to pip install ollama.
- Make sure that `horoscope.py` and `config.py` are in the same directory.
- Run `horoscope.py`
  
## HOW IT WORKS
- `horoscope.py` uses the `config.py` to pull a random attribute from the sign chosen.
- This attribute will be added to the prompt being fed into the model.
- EXAMPLE : The script chose this for a Leo "can come across as overly proud and boastful, believing they are superior to others."
- The full prompt will then be `Create a very short, vague, and negative second-person narrative about a person who can come across as overly proud and boastful, believing they are superior to others. Never use the words "me", "I", or "my". Be Sarcastic and negative. Start with "Today you will"`
- The model will then create the horoscope to be displayed.

## HOW I USE IT
- I use it in my portfolio website as part of the react/flask backend. [Website](http://38.125.229.163:3000/horrible-horoscope)

## KNOWN BUGS
- Instead of referring to you, the reader, it mentions another person with the horoscope you chose. It will say you will meet this person instead of this person being you.
This can be fixed by a bigger model, but at the cost of run time.


## Requirements

-   [Python](https://www.python.org) \>= 2.7, 3.4+
-   [Flask](https://flask.palletsprojects.com/en/3.0.x/) \>= 3.0.3

### P.S.

Please drop me a note with any feedback you have.

**Joel**
