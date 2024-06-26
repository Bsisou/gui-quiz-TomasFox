from tkinter import *
from PIL import Image, ImageTk
import random

class Quiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Geography Quiz")
        self.master.geometry("750x500")

        # Background image
        self.bg = PhotoImage(file="MAP.png")
        self.bglabel = Label(self.master, image=self.bg)
        self.bglabel.place(x=0, y=0)

        # Initialize quiz data
        self.q_n_a = {
            1: ["What is the capital of France?", "Paris", "London", "Berlin", "Madrid", 1],
            2: ["What is the currency of Japan?", "Yen", "Dollar", "Euro", "Pound", 1],
            3: ["What is the highest mountain in the world?", "Mount Everest", "K2", "Makalu", "Cho Oyu", 1],
            4: ["What is the largest ocean in the world?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
            5: ["What is the largest country in the world \n by land area?", "Russia", "Canada", "China", "USA", 1],
            6: ["What is the currency of Brazil?", "Real", "Dollar", "Euro", "Pound", 1],
            7: ["What is the smallest country in the world \n by land area?", "Vatican City", "Monaco", "Nauru", "Tuvalu", 1]
        }

        self.asked = []
        self.qnum = self.randomiser()

        # Initialize score
        self.score = 0

        # Show the start page
        self.start_page()

    def randomiser(self):
        qnum = random.randint(1, 7)
        if qnum not in self.asked:
            self.asked.append(qnum)
            return qnum
        else:
            return self.randomiser()

    def start_page(self):
        self.heading = Label(self.master, text="Welcome to the quiz", background="#e1d9bb", font=("comfortaa", 40))
        self.heading.place(x=100, y=10)

        self.label_username = Label(self.master, text="Enter your name: ", background="#e1d9bb", font=("arial", 18))
        self.label_username.place(x=250, y=200)

        self.name_entry = Entry(self.master)
        self.name_entry.place(x=285, y=245)

        self.continuebtn = Button(self.master, text="Continue", font=("arial", 20), background="#9ED5A8", command=self.start_quiz)
        self.continuebtn.place(x=280, y=380)

    def start_quiz(self):
        username = self.name_entry.get()
        self.names = [username]
        self.master.destroy()
        self.display_question()

    def display_question(self):
        self.quiz_window = Tk()
        self.quiz_window.title("Geography Quiz")
        self.quiz_window.geometry("750x500")

        # Background image
        self.bg = PhotoImage(file="MAP.png")
        self.bglabel = Label(self.quiz_window, image=self.bg)
        self.bglabel.place(x=0, y=0)

        bg_colour = "#e1d9bb"
        question_text = self.q_n_a[self.qnum][0]

        self.question_label = Label(self.quiz_window, text=question_text, bg="orange", font=("arial", 20))
        self.question_label.place(x=135, y=80)

        self.var1 = IntVar()
        self.rb1 = Radiobutton(self.quiz_window, text=self.q_n_a[self.qnum][1], value=1, bg="#AFE1AF", font=("arial", 15), variable=self.var1)
        self.rb1.place(x=200, y=150)
        self.rb2 = Radiobutton(self.quiz_window, text=self.q_n_a[self.qnum][2], value=2, bg="#E97451", font=("arial", 15), variable=self.var1)
        self.rb2.place(x=200, y=185)
        self.rb3 = Radiobutton(self.quiz_window, text=self.q_n_a[self.qnum][3], value=3, bg="yellow", font=("arial", 15), variable=self.var1)
        self.rb3.place(x=400, y=150)
        self.rb4 = Radiobutton(self.quiz_window, text=self.q_n_a[self.qnum][4], value=4, bg="#89CFF0", font=("arial", 15), variable=self.var1)
        self.rb4.place(x=400, y=185)

        self.confirm_button = Button(self.quiz_window, text="Confirm", bg="forestgreen", command=self.process_answer)
        self.confirm_button.place(x=295, y=380)

        self.quiz_window.mainloop()

    def process_answer(self):
        selected_option = self.var1.get()
        correct_answer = self.q_n_a[self.qnum][5]

        if selected_option == correct_answer:
            self.score += 1

        # After processing answer, move to next question or end quiz
        self.qnum = self.randomiser()
        self.quiz_window.destroy()
        if self.qnum == 1 or 2 or 3 or 4 or 5 or 6 or 7:  # Add condition to check if quiz is finished
            self.display_question()
        else:
            self.show_score()

    def show_score(self):
        score_window = Tk()
        score_window.title("Quiz Result")
        score_window.geometry("400x300")

        score_label = Label(score_window, text=f"Congratulations {self.names[0]}!\nYour score is {self.score}/7", font=("arial", 20))
        score_label.pack(pady=50)

        score_window.mainloop()

# Start the application
if __name__ == "__main__":
    page = Tk()
    app = Quiz(page)
    page.mainloop()
