from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from apicall import apiCall
from fastapi.middleware.cors import CORSMiddleware
from main import run_tts


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicRequest(BaseModel):
    topic: str

@app.post("/generate")
def generate_topic_audio(request: TopicRequest):
    topic = request.topic
    print(topic)

    if not topic:
        return JSONResponse(content={"error": "No topic provided"}, status_code=400)
    
    text = apiCall(topic)
    if text:
        print(text)



    try:
        run_tts(text=text, voice_name="MALE_FUNNY", output_file="output.mp3", play=False)
        print('response generated')
    except Exception as e:
        return JSONResponse(content={"error tts": str(e)}, status_code=500)


  
    return FileResponse("output.mp3", media_type="audio/mpeg", filename="output.mp3")