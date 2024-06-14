from asciimatics.screen import Screen

def display_scene():
  screen = Screen()
  screen.clear()
  screen.print_at("A woman sits on her couch, holding a sleek device.", 1, 1, color=Screen.WHITE)
  screen.print_at("The device glows with a soft blue light.", 2, 1, color=Screen.CYAN)
  screen.refresh(True)
  screen.wait(1000)  # Wait for 1 second

display_scene()
