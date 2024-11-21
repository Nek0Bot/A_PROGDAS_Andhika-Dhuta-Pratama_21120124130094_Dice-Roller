import tkinter as tk
import random
from PIL import Image, ImageTk

class DiceRollerApp:
    # Definisi Kelas & constructor
    def __init__(self, master):
        self.master = master
        master.title("Dice Roller")
        master.configure(bg="gray")  

        # Label utama
        self.label = tk.Label(master, text="Roll ze dice!", font=("Helvetica", 16), bg="gray", fg="white")
        self.label.pack(pady=20)

        # Jumlah dadu
        self.dice_count_label = tk.Label(master, text="Jumlah dadu:", font=("Helvetica", 14), bg="gray", fg="white")
        self.dice_count_label.pack(pady=5)

        self.dice_count_entry = tk.Entry(master, font=("Helvetica", 14), bg="lightgray", fg="black")
        self.dice_count_entry.pack(pady=5)

        # Tombol Roll
        self.roll_button = tk.Button(master, text="Roll", command=self.roll_dice, font=("Helvetica", 14), bg="black", fg="white")
        self.roll_button.pack(pady=10)
        
        # Hasil roll
        self.result_label = tk.Label(master, text="", font=("Helvetica", 18), bg="gray", fg="white")
        self.result_label.pack(pady=20)

        # Frame untuk gambar dadu
        self.dice_images_frame = tk.Frame(master, bg="gray")
        self.dice_images_frame.pack(pady=10)

        # Label history hasil
        self.last_rolls_label = tk.Label(master, text="5 Hasil Roll Terakhir:", font=("Helvetica", 14), bg="gray", fg="white")
        self.last_rolls_label.pack(pady=10)

        self.last_rolls_display = tk.Text(master, font=("Helvetica", 12), bg="gray", fg="white", height=8, width=50, state="disabled")
        self.last_rolls_display.pack(pady=5)

        # label total jumlah dadu
        self.total_dice_rolled_label = tk.Label(master, text="Total Dadu Dilempar: 0", font=("Helvetica", 14), bg="gray", fg="white")
        self.total_dice_rolled_label.pack(side="right", padx=20)

        # Tombol Quit
        self.quit_button = tk.Button(master, text="Quit", command=master.quit, font=("Helvetica", 14), bg="black", fg="white")
        self.quit_button.pack(pady=10)

        # memasukan & resize gambar dadu
        self.die_faces = []
        for i in range(1, 7):
            img = Image.open(f"d6_{i}.png")
            img = img.resize((100, 100), Image.LANCZOS)
            self.die_faces.append(ImageTk.PhotoImage(img))

        self.last_rolls = []  # List untuk menyimpan 5 hasil terakhir
        self.total_dice_rolled = 0  # Counter untuk total dadu yang telah dilempar

    # function roll dadu
    def roll_dice(self):
        try:
            num_dice = int(self.dice_count_entry.get())
            if num_dice < 1:
                self.result_label.config(text="Angka harus positif!", fg="red")
                return
            if num_dice > 10:
                self.result_label.config(text="Jumlah melebihi batas!", fg="red")
                return
        except ValueError:
            self.result_label.config(text="Masukkan angka!", fg="red")
            return

        #menghasilkan  angka acak dalam range
        results = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(results)

        # pesan berdasarkaan hasil roll dadu
        if total > 4.5 * num_dice:
            message = "GG king"
            color = "gold"
        elif total < 2.5 * num_dice:
            message = "Kurang hoki pakde"
            color = "red"
        else:
            message = "Nice roll!"
            color = "white"

        message += f"\nRolls: {', '.join(map(str, results))} | Total: {total}"
        self.result_label.config(text=message, fg=color)

        # Update total dice rolled
        self.update_total_dice_rolled(num_dice)

        # Update hasil terakhir
        self.update_last_rolls(results, total, color)

        for widget in self.dice_images_frame.winfo_children():
            widget.destroy()

        for result in results:
            die_label = tk.Label(self.dice_images_frame, image=self.die_faces[result - 1], bg="gray")
            die_label.pack(side="left", padx=5)

    def update_total_dice_rolled(self, num_dice):
        self.total_dice_rolled += num_dice
        self.total_dice_rolled_label.config(text=f"Total Dadu Dilempar: {self.total_dice_rolled}")

    def update_last_rolls(self, results, total, color):
        roll_summary = f"Rolls: {', '.join(map(str, results))} | Total: {total}"
        self.last_rolls.append((roll_summary, color))
        if len(self.last_rolls) > 5:
            self.last_rolls.pop(0)  # Hapus hasil paling lama jika lebih dari 5

        # menampilkan hasil terakhir di Text widget
        self.last_rolls_display.config(state="normal")
        self.last_rolls_display.delete("1.0", tk.END)  # Hapus semua teks lama

        for roll_summary, color in self.last_rolls:
            self.last_rolls_display.insert(tk.END, roll_summary + "\n", color)

        # menambahkan tag warna untuk setiap teks
        for _, color in self.last_rolls:
            self.last_rolls_display.tag_configure(color, foreground=color)

        self.last_rolls_display.config(state="disabled")  # Disable editing

# membuat window & menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    dice_roller_app = DiceRollerApp(root)
    root.mainloop()
