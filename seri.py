import webbrowser
import os
import sys
import pyautogui

def clear_cmd():
    os.system('cls')

def open_app(app) :
    pyautogui.moveTo(600,1050,duration=0)
    pyautogui.click(600, 1050, interval=0.01)
    pyautogui.typewrite(app)
    pyautogui.moveTo(600, 300,duration=0)
    pyautogui.click(600, 300,duration=0.001)

    
def open_web(url) :
    web = f"https://www.{url}.com"
    webbrowser.open(web)

def start() :
    rep = True
    while (rep) :
        clear_cmd()
        print("Would you like to open an app or a web? ") 
        ans = input()
        while ans != "app" and ans != "web" :
            print("try again")
            ans = input()
            if "stop" in ans :
                break

        if ans == "app":
            print("Alright, what app would you like to open ") 
            app = input()
            open_app(app)
        if ans == "web" :
            print("Alright, what website would you like to visit ") 
            web = input()
            open_web(web)
        print("Anything else? ")
        res = input()
        if res.lower() != "yes" :
            rep = False
        

if __name__ == '__main__' :
    start()
print("Glad to help you!")