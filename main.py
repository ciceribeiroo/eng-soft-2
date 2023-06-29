# This is a sample Python script.
from fastapi import FastAPI
from minio import Minio
from moviepy.video.io.VideoFileClip import VideoFileClip

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/convert/{bucketName}/{fileName}")
async def convert_mp4_to_mp3(bucketName: str, fileName: str):
    try:
        f_name = "/temp/downloads/teste.mp4"
        f_name_converted = "/temp/downloads/teste.mp3"

        client = Minio("minio:9000", access_key="ROOTUSER", secret_key="ENGSOFTWARE", secure=False)
        client.fget_object(bucketName, fileName, f_name)

        audio = video_to_audio(f_name, f_name_converted)

        client.fput_object(bucketName, f"{fileName.split('.')[0]}_converted.mp3", f_name_converted)

        return {"message": "Converted"}
    except Exception:
        return {"message": "Error"}



def video_to_audio(video_path, audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()

    return audio_clip