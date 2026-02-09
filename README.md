Poniżej masz **gotowe README.md po angielsku**, czyste, zrozumiałe i bez marketingowego bełkotu. Takie, które nie wstyd wrzucić na GitHuba.

---

# 🇵🇱🇷🇺 Polish–Russian Flashcard App (Tkinter)

A simple desktop flashcard application built with **Python**, **Tkinter**, and **Pandas** to help learn Russian–Polish vocabulary using spaced repetition principles.

The app displays a Russian word first and automatically flips the card after a few seconds to reveal the Polish translation. Users can mark words as known or unknown, gradually reducing the learning set.

---

## ✨ Features

* Flashcard-style vocabulary learning
* Automatic card flip (Russian → Polish)
* Random word selection from CSV data
* Ability to remove known words from the learning pool
* Clean and minimal Tkinter GUI
* CSV-based data storage (easy to extend or replace)

---

## 🧠 How It Works

1. A random Russian word is displayed.
2. After 5 seconds, the card flips and shows the Polish translation.
3. Buttons allow the user to:

   * ❌ **Mark as incorrect** – the word stays in the learning pool
   * ✅ **Mark as correct** – the word is removed and saved to a separate CSV file
4. The next word is shown automatically.

This allows the app to gradually focus only on words that still need practice.

---

## 📂 Project Structure

```
.
├── main.py
├── RU_PL - Arkusz1.csv
├── wordl_to_learn.csv
├── card_front.png
├── card_back.png
├── right.png
├── wrong.png
└── README.md
```

---

## 📄 CSV Format

The vocabulary file must contain the following columns:

```csv
Rosyjski,Polski
привет,cześć
дом,dom
```

* `Rosyjski` – Russian word
* `Polski` – Polish translation

---

## 🛠 Requirements

* Python 3.9+
* pandas

Install dependencies:

```bash
pip install pandas
```

Tkinter is included by default with most Python installations.

---

## ▶️ Running the App

```bash
python main.py
```

Make sure all image files and CSV files are in the same directory as the script.

---

## 🚧 Known Limitations

* No persistence of progress between sessions (except removed words CSV)
* CSV file is loaded fully into memory
* No language configuration (fixed Russian → Polish)
* Basic error handling

These are deliberate trade-offs to keep the project simple and educational.

---

## 🎯 Educational Purpose

This project was built as a learning exercise to practice:

* Tkinter GUI programming
* Event-driven logic
* Timers (`after`)
* State management
* Working with CSV data using Pandas

It is intentionally kept simple and readable rather than over-engineered.

---

## 📌 Possible Improvements

* Save progress between sessions
* Add multiple language pairs
* Shuffle timing based on difficulty
* Add statistics and progress tracking
* Package as a standalone app (e.g. with Nuitka or PyInstaller)

---

## 📜 License

MIT License.
Use it, modify it, break it, learn from it.

---

Jeśli chcesz:

* wersję **bardziej „produktową”**
* README pod **rekrutację**
* albo **ostrą krytykę architektury** i co byś poprawił jako kolejny krok

to wtedy już jedziemy bez litości.
