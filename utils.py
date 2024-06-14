# Imports (assuming you have internet access)
import subprocess

# List of Dependencies (modify as needed)
dependencies = ["requests"]  # Example dependency (for potential future use)

def install_dependencies():
  """Installs dependencies using pip."""
  for dependency in dependencies:
    command = f"pip install {dependency}"
    subprocess.run(command.split(), check=True)
  print("Dependencies installed successfully!")

def generate_prompts(scenes, prompts):
  """Prints scene titles and prompts for video creation."""
  for i in range(len(scenes)):
    print(f"Scene {i+1}: {scenes[i]}")
    print(f"\tPrompt: {prompts[i]}")
    print()

# Scene Titles
scenes = [
    "Intro - Sterile Apartment",
    "AIA Headquarters - Server Room",
    "Emma's Apartment - Device Warning",
    "AIA Headquarters - Chloe Working",
    "Emma's Apartment - Dr. Kapoor (Virtual)",
    "Crowded Clinic - Long Wait",
    "AIA Headquarters - Press Conference",
    "Montage - Positive Outcomes",
    "News Report - Protests erupt",
    "AIA Headquarters - Board Meeting",
    "Emma's Apartment - Talking to Dr. Kapoor",
    "Cityscape with AIA Logo - Final Text"
]

# Text Prompts for Each Scene
prompts = [
    "A woman in a sleek apartment uses a minimalist medical device. A gentle blue light emanates from it.",
    "A massive server room with rows of blinking lights and whirring fans. A programmer monitors a complex algorithm.",
    "A woman looks at a medical device with a red light displaying a warning. She seems surprised.",
    "A young woman works on complex code in a high-tech office. Screens display data and algorithms.",
    "A warm and familiar face of an elderly doctor appears on a screen. A younger woman talks to the doctor.",
    "A crowded clinic waiting room with frustrated people. Signs of long wait times and lack of staff.",
    "A young woman speaks at a press conference about a new healthcare system with an impressive backdrop.",
    "Fast-paced montage of positive healthcare outcomes: a woman feeling better, a family video consultation, a drone delivering medicine.",
    "News report shows protests outside a hospital. People chant slogans against AI healthcare.",
    "A board room meeting with serious expressions. A young woman presents about an ethical framework.",
    "A woman smiles while talking to a virtual doctor on a medical device. The doctor's face is warm and reassuring.",
    "A wide shot of a city skyline at night. The AIA logo shines brightly on a skyscraper. Text overlay: AIA. The future of healthcare is here. Are you ready?"
]

# Check for pip command (modify based on your OS)
if subprocess.run(["pip", "--version"], capture_output=True).returncode == 0:
  # If pip exists, install dependencies (uncomment if needed)
  # install_dependencies()
  # Generate prompts
  generate_prompts(scenes, prompts)
else:
  print("Error: pip command not found. Please install Python and ensure pip is available.")
