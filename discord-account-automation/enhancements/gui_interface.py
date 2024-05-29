from tkinter import Tk, Label, Entry, Button

class GUIInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Discord Account Automation GUI")
        self.window.geometry("400x300")

        self.label_email = Label(self.window, text="Email:")
        self.label_email.pack()
        self.entry_email = Entry(self.window)
        self.entry_email.pack()

        self.label_username = Label(self.window, text="Username:")
        self.label_username.pack()
        self.entry_username = Entry(self.window)
        self.entry_username.pack()

        self.label_password = Label(self.window, text="Password:")
        self.label_password.pack()
        self.entry_password = Entry(self.window, show="*")
        self.entry_password.pack()

        self.label_birthdate = Label(self.window, text="Birthdate:")
        self.label_birthdate.pack()
        self.entry_birthdate = Entry(self.window)
        self.entry_birthdate.pack()

        self.button_submit = Button(self.window, text="Submit", command=self.submit_form)
        self.button_submit.pack()

    def submit_form(self):
        email = self.entry_email.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        birthdate = self.entry_birthdate.get()

        # Add logic here to use the input data for account creation

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = GUIInterface()
    gui.run()