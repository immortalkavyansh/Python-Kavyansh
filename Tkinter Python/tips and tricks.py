from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("PythonWithKavi")
root.wm_iconbitmap("D:\\PycharmProjects\\tkinter gui\\logo.ico")
root.config(bg="light green")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")
Button(text="Close", command=root.destroy()).grid()
root.mainloop()
