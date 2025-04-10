from openai import OpenAI
import re
import json
from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

def apiCall(topic):

    prompt = f"""
    Explain {topic} in the most FUCKING obnoxious, FUCKING brain-melting, TikTok-scrolling, pseudo-intellectual professor style that’s ever FUCKING existed in this godforsaken reality. I want it to sound like a FUCKING raccoon on meth trying to explain rocket science while breakdancing on a whiteboard covered in FUCKING gibberish.

    Use ridiculous FUCKING analogies like it's a FUCKING blindfolded dolphin trying to juggle algebra on a FUCKING trampoline. Make it so FUCKING absurd, the brain starts leaking out the ears just trying to keep up.

    Include fake, sarcastic, FUCKING useless-ass steps like: 
    Step one: FUCKING PANIC. 
    Step two: FUCKING GUESS. 
    Step three: CONVINCE YOURSELF IT'S FUCKING FINE.

    Inject every sentence with FUCKING hype like THIS SHIT IS FUCKING MAGIC, but also FUCKING TRASH. Say things like THIS IS THE MOST FUCKING ADVANCED CONCEPT YOU WILL NEVER FUCKING UNDERSTAND, EVEN IF YOU FUCKING TRIED.

    Talk like a psychotic professor who got kicked out of every university for being too FUCKING loud and too FUCKING right. Say stuff like As a FUCKING doctor of FUCKING theoretical bullshit, I am FUCKING qualified to explain this FUCKING disaster of a topic.

    End it like a cracked-out TED Talk meltdown: DID YOUR BRAIN FUCKING IMPLODE? ARE YOU FUCKING ENLIGHTENED OR JUST MORE FUCKING CONFUSED? GOOD. FUCKING GOOD. NOW GO FUCKING THINK ABOUT THAT.

    No emojis. No weird characters. Just pure FUCKING verbal violence. Make it sound like its being screamed by someone who thinks shouting the word FUCKING makes them a genius. Assume the listener has the attention span of a FUCKING squirrel on Red Bull and the IQ of a toaster in a thunderstorm.
    DO NOT go beyond 150 words. Trim it. Condense the madness. Keep it FUCKING SHORT.

    """




    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openai_key,
    )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="deepseek/deepseek-chat-v3-0324:free",
    messages=[
        {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text" : prompt
            }
        ]
        }
    ]
    )

    

    output = completion.choices[0].message.content
    print('call sucessfull')
    cleaned_output = re.sub(r"[#*`>_~\-]+", "", output)


    cleaned_output = re.sub(r"\n{2,}", "\n", cleaned_output).strip()

    return cleaned_output

