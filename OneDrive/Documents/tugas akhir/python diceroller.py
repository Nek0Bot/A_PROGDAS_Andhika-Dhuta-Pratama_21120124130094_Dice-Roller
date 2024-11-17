import tkinter as tk
import random
from PIL import Image, ImageTk  
class DiceRollerApp:
    def __init__(self, master):
        self.master = master
        master.title("Dice Roller")

        self.label = tk.Label(master, text="Roll ze dice!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.dice_count_label = tk.Label(master, text="jumlah dadu:", font=("Helvetica", 14))
        self.dice_count_label.pack(pady=5)

        
        self.dice_count_entry = tk.Entry(master, font=("Helvetica", 14))
        self.dice_count_entry.pack(pady=5)

        self.roll_button = tk.Button(master, text="Roll", command=self.roll_dice, font=("Helvetica", 14))
        self.roll_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 18))
        self.result_label.pack(pady=20)

        
        self.dice_images_frame = tk.Frame(master)
        self.dice_images_frame.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, font=("Helvetica", 14))
        self.quit_button.pack(pady=10)

        
        self.die_faces = []
        for i in range(1, 7):
            img = Image.open(f"d6_{i}.png")
            img = img.resize((100, 100), Image.LANCZOS)
            self.die_faces.append(ImageTk.PhotoImage(img))

    def roll_dice(self):
        try:
            num_dice = int(self.dice_count_entry.get())
            if num_dice < 1:
                self.result_label.config(text="Angka harus positif!")   
                return
            if num_dice > 10:
                self.result_label.config(text="Jumlah melebihi batas!")
                return
        except ValueError:
            self.result_label.config(text="Masukan angka!")
            return

        results = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(results)

        
        if total > 5 * num_dice:
            message = "GG king"
        elif total < 2 * num_dice:
            message = "Kurang hoki pakde"    
        else:
            message = "Nice roll!"

        
        message += f"\nRolls: {', '.join(map(str, results))} | Total: {total}"

        
        self.result_label.config(text=message)

        
        for widget in self.dice_images_frame.winfo_children():
            widget.destroy()

        
        for result in results:
            die_label = tk.Label(self.dice_images_frame, image=self.die_faces[result - 1])
            die_label.pack(side="left", padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    dice_roller_app = DiceRollerApp(root)
    root.mainloop()
