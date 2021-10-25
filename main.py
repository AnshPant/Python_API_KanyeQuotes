from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest") #receiving response from the api
    response.raise_for_status() #raising status for all king provided in request liberary
    data = response.json() #store data in json formate in data
    quote = data["quote"] #accessig quote element in the json
    canvas.itemconfig(quote_text, text=quote) #this will config the quote text fixed in canva


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()