# Club Penguin Auto Mine
from tkinter import Button, Label, Message, PhotoImage, Tk, messagebox
import random
import time
import pyautogui


def auto_miner_gui():
    global window
    window = Tk()
    icon = PhotoImage(file="./lib/logo.png")
    window.geometry("500x300")
    window.title("Auto Miner - @ViniVentura")
    window.iconphoto(True, icon)

    lable = Label(window, text="Configurar Coordenadas:")
    lable.pack()

    firstButton = Button(window, text="Primeira Coordenada")
    firstButton.pack()
    secondButton = Button(window, text="Segunda Coordenada")
    secondButton.pack()
    runButton = Button(window, text="Ficar Rico!")
    runButton.pack()

    firstButton.config(command=first_movement_config)
    secondButton.config(command=second_momovement_config)
    runButton.config(command=run_app)

    window.mainloop()


def first_movement_config():
    messagebox.showinfo("Primeira Coordenada",
                        "Mova seu cursor até a primeira posição do seu pinguim.")
    messagebox.showwarning("Segura ai!",
                           "Após clicar em Ok, você terá 3 segundos para deixar o cursor parado na posição desejada.")
    time.sleep(3)
    x, y = pyautogui.position()
    global secondPosition
    secondPosition = int(str(y))
    global firstPosition
    firstPosition = int(str(x))
    x = str(x).rjust(4)
    y = str(y).rjust(4)
    message = Message(
        window, text="Primeira coordenada salva em: (" + y + "," + x + " )", width=250)
    message.pack()


def second_momovement_config():
    messagebox.showinfo("Primeira Coordenada",
                        "Mova seu cursor até a primeira posição do seu pinguim.")
    messagebox.showwarning("Segura ai!",
                           "Após clicar em Ok, você terá 3 segundos para deixar o cursor parado na posição desejada.")
    time.sleep(3)
    x, y = pyautogui.position()
    global secondPostion2
    secondPostion2 = int(str(y))
    global firstPostion2
    firstPostion2 = int(str(x))
    x = str(x).rjust(4)
    y = str(y).rjust(4)
    message2 = Message(
        window, text="Segunda coordenada salva em: (" + y + "," + x + " )", width=250)
    message2.pack()


def run_app():
    while True:
        xCoordinates = random.randint(secondPosition, firstPosition)
        yCoordinates = random.randint(secondPostion2, firstPostion2)

        pyautogui.click(xCoordinates, yCoordinates)
        time.sleep(3)
        pyautogui.press("d")
        time.sleep(10)


auto_miner_gui()
