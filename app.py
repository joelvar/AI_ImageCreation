from auth import auth_token
import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageTk
import requests

import openai

openai.api_key = auth_token

app = tk.Tk()
app.geometry("532x612")
app.title("Image Generation")
ctk.set_appearance_mode("dark")


main_image = tk.Canvas(app,width = 512, height=492)
main_image.place(x=10,y=110)

prompt_input = ctk.CTkEntry(
    master = app,
    height = 40,
    width = 512,
    font=("Roboto Medium", -16),
    text_color="black",
    fg_color="white",
    placeholder_text="Enter a prompt:",
)
prompt_input.place(x=10,y=10)

def generate_image():
    global tk_img
    global img

    prompt = prompt_input.get()
    response = openai.Image.create(prompt = prompt, n = 1, size = "512x512")
    image_url = response["data"][0]["url"]
    img = Image.open(requests.get(image_url,stream = True).raw)
    tk_img = ImageTk.PhotoImage(img)
    main_image.create_image(0,0,anchor = tk.NW, image= tk_img)

def save_image():
    prompt = prompt_input.get().replace(" ","_")
    img.save(f"img/{prompt}.png")


magic_button = ctk.CTkButton(
    master = app,
    height = 40,
    width = 120,
    font = ("Arial",20),
    text_color="white",
    fg_color=("white","gray38"),
    command=generate_image,
)
magic_button.configure(text = "Create Image")
magic_button.place(x=123,y = 60)

save_button = ctk.CTkButton(
    master = app,
    height = 40,
    width = 120,
    font = ("Arial",20),
    text_color="white",
    fg_color=("white","gray38"),
    command=save_image,
)
save_button.configure(text = "Save Image")
save_button.place(x=276,y = 60)

app.mainloop()

