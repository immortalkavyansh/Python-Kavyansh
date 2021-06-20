from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__ == '__main__':
    speak("this speaking machine is the best thing in my life, thank you win32for making this beautiful function")
