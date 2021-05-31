from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Scrollbar tutorial")
# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2 scrollbar.config(command=widget.yview)



# listbox = Listbox(root, yscrollcommand = scrollbar.set)
# for i in range(344):
#     listbox.insert(END, f"Item {i}")

# listbox.pack(fill="both",padx=22 )
text = Text(root, height=700)
text.pack(fill=BOTH)


root.mainloop()
