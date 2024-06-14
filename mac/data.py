from moviepy.editor import *

# Text for each scene with titles
clips = [
    Clip("white.jpg", text="AIA - All-Inclusive Access", color='white', fontsize=70, font="Arial"),
    Clip("apartment_sterile.jpg", text="Scene 1: Diagnosis", color='black', fontsize=40, font="Arial",  duration=2).set_pos((100,20)),
    Clip("server_room.jpg", text="Scene 2: AIA Headquarters", color='black', fontsize=40, font="Arial",  duration=3).set_pos((100,20)),
    Clip("apartment_living.jpg", text="Scene 3: Dr. Anya Kapoor", color='black', fontsize=40, font="Arial",  duration=4).set_pos((100,20)),
    Clip("clinic_crowded.jpg", text="Scene 4: The Problem", color='black', fontsize=40, font="Arial",  duration=2).set_pos((100,20)),
    Clip("ai_hq_press.jpg", text="Scene 5: AIA - The Solution", color='black', fontsize=40, font="Arial",  duration=3).set_pos((100,20)),
    Clip("montage_clips.mp4", duration=5),  # Replace with your montage clip
    Clip("protest_hospital.jpg", text="Scene 7: The Challenge", color='black', fontsize=40, font="Arial",  duration=2).set_pos((100,20)),
    Clip("ai_hq_boardroom.jpg", text="Scene 8: Building Trust", color='black', fontsize=40, font="Arial",  duration=4).set_pos((100,20)),
    Clip("apartment_living.jpg", text="Scene 9: The Future", color='black', fontsize=40, font="Arial",  duration=3).set_pos((100,20)),
    Clip("city_night.jpg", text="AIA. The future of healthcare is here. Are you ready?", color='white', fontsize=50, font="Arial",  duration=5).set_pos((100,50)),
]

# Generate audio using gtts (replace with your preferred TTS engine)
from gtts import gTTS

def generate_speech(text):
  speech = gTTS(text=text, lang='en')
  speech.save("temp.mp3")
  return AudioFileClip("temp.mp3").set_duration(len(text) / 150)  # Adjust speed as needed

# Add audio narration to each clip
for clip in clips[1:]:
  voice = generate_speech(clip.text)
  clip = clip.set_audio(voice)

# Concatenate all clips
final_clip = concatenate_videoclips(clips)

# Write the final video with background music (replace with your music)
final_clip.write_videofile("AIA_Trailer.mp4", fps=24, audio_bitrate="128k", background_music="path/to/your/music.mp3")

print("Trailer generated: AIA_Trailer.mp4")
