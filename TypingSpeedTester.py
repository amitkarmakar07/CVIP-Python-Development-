import tkinter as tk
import random
import time

class TSTApp:
    def __init__(self, r):
        self.r = r
        self.r.title("Typing Speed Tester")

        self.st = [
            "The quick brown fox jumps over the lazy dog.",
            "Type as fast as you can!",
            "Practice makes perfect.",
            "Python is a great programming language.",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Innovation distinguishes between a leader and a follower."
        ]

        self.gt = tk.Text(r, wrap=tk.WORD, width=60, height=10)
        self.gt.pack()

        self.ut = tk.Text(r, wrap=tk.WORD, width=60, height=10, state=tk.DISABLED)
        self.ut.pack()

        self.sb = tk.Button(r, text="Start", command=self.start)
        self.sb.pack()

        self.sob = tk.Button(r, text="Stop", command=self.stop, state=tk.DISABLED)
        self.sob.pack()

        self.w = tk.Label(r, text="WPM: ")
        self.w.pack()

        self.a = tk.Label(r, text="Accuracy: ")
        self.a.pack()

        self.t = ""
        self.stime = 0

    def start(self):
        self.gt.delete("1.0", tk.END)
        self.ut.config(state=tk.NORMAL)
        self.ut.delete("1.0", tk.END)
        self.t = random.choice(self.st)
        self.gt.insert("1.0", self.t)
        self.stime = time.time()
        self.sb.config(state=tk.DISABLED)
        self.sob.config(state=tk.NORMAL)
        self.rb.config(state=tk.DISABLED)
        self.ut.config(state=tk.NORMAL)

    def stop(self):
        self.ut.config(state=tk.DISABLED)
        et = time.time()
        tt = self.ut.get("1.0", tk.END)
        w, a = self.calculate_speed_and_accuracy(tt, et - self.stime)
        self.w.config(text=f"WPM: {w:.2f}")
        self.a.config(text=f"Accuracy: {a:.2f}%")
        self.sb.config(state=tk.NORMAL)
        self.sob.config(state=tk.DISABLED)
        self.rb.config(state=tk.NORMAL)

    def reset(self):
        self.gt.delete("1.0", tk.END)
        self.ut.config(state=tk.NORMAL)
        self.ut.delete("1.0", tk.END)
        self.w.config(text="WPM: ")
        self.a.config(text="Accuracy: ")
        self.rb.config(state=tk.DISABLED)

    def calculate_speed_and_accuracy(self, tt, et):
        tw = tt.split()
        rw = self.t.split()
        nw = len(rw)
        cw = sum(1 for t, r in zip(tw, rw) if t == r)
        a = (cw / nw) * 100
        em = et / 60
        wpm = (len(tt) / 5) / em
        return wpm, a

if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("800x600")
    app = TSTApp(r)
    r.mainloop()
