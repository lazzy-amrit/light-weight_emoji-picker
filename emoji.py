import tkinter as tk
import subprocess

active_window = subprocess.check_output(
    ["xdotool", "getactivewindow"]
).decode().strip()

categories = {
    "🙂": [
        "😀","😁","😂","🤣","😃","😄","😅","😆","😉","😊",
        "🙂","🙃","😍","😘","😎","🤔","😐","🙄","😴","😭",
        "😡","🤯","😇","😈","🤓","🥳","😬","😳","😱","🥶",
        "🥵","😜","😕","😔","😣","😖","😫","😤","😩","😵",
        "🤠","🤡","🤫","🤭","🫠","🫡","🤪","😶‍🌫️"
    ],
    "👍": [
        "👍","👎","👌","✌️","🤞","🤘","👏","🙌","🙏","💪",
        "👊","🤙","✋","🖐️","🤝","🫶","🤟","🤜","🤛","✊"
    ],
    "❤️": [
        "❤️","💔","💯","🔥","✨","⭐","⚡","💀","☠️","🎉",
        "🎶","🎵","🌙","☀️","💎","🖤","🤍","💥","💫","🌟","🚀"
    ]
}

def type_emoji(emoji):
    subprocess.Popen([
        "xdotool",
        "windowactivate", "--sync", active_window,
        "type", "--delay", "0", emoji
    ])

def on_hover(e):
    e.widget["bg"] = "#3a3a3a"

def off_hover(e):
    e.widget["bg"] = "#2a2a2a"

def load_category(cat):
    for widget in scroll_frame.winfo_children():
        widget.destroy()

    emojis = categories[cat]
    columns = 6

    for i, emoji in enumerate(emojis):
        btn = tk.Button(
            scroll_frame,
            text=emoji,
            font=("Segoe UI Emoji", 12),
            width=2,
            height=1,
            bg="#2a2a2a",
            fg="white",
            activebackground="#3a3a3a",
            bd=0,
            highlightthickness=0,
            relief="flat",
            command=lambda e=emoji: type_emoji(e)
        )
        btn.grid(row=i//columns, column=i%columns, padx=3, pady=3)
        btn.bind("<Enter>", on_hover)
        btn.bind("<Leave>", off_hover)

    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Emoji")
root.geometry("330x280")
root.configure(bg="#1b1b1b")
root.resizable(False, False)
root.attributes("-topmost", True)

# Category bar
top_frame = tk.Frame(root, bg="#1b1b1b")
top_frame.pack(pady=4)

for cat in categories.keys():
    btn = tk.Button(
        top_frame,
        text=cat,
        font=("Segoe UI Emoji", 11),
        bg="#1b1b1b",
        fg="white",
        activebackground="#2a2a2a",
        bd=0,
        highlightthickness=0,
        relief="flat",
        command=lambda c=cat: load_category(c)
    )
    btn.pack(side="left", padx=6)

# Scroll area
canvas = tk.Canvas(root, bg="#1b1b1b", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scroll_frame = tk.Frame(canvas, bg="#1b1b1b")

scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True, padx=(6,0))
scrollbar.pack(side="right", fill="y")

# Proper Linux scrolling
def scroll_up(event):
    canvas.yview_scroll(-1, "units")

def scroll_down(event):
    canvas.yview_scroll(1, "units")

canvas.bind_all("<Button-4>", scroll_up)
canvas.bind_all("<Button-5>", scroll_down)

load_category("🙂")

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()