# 🎤 Voice to Sketch AI

> Speak your imagination — and let AI turn it into art.

*Voice to Sketch AI* is a web application that allows users to speak visual prompts (e.g., “draw a spaceship in the desert”) and receive AI-generated images in multiple artistic styles like Pencil Sketch, Watercolor, Oil Painting, and more.

---

## ✨ Features

* 🎙️ *Voice Recognition:* Converts your voice into a text prompt.
* 🧠 *AI Sketch Generation:* Uses Hugging Face's Stable Diffusion API to draw.
* 🖼️ *Multiple Styles:* Choose from Pencil Sketch, Watercolor, Oil Painting, Realistic, or Cartoon.
* 📜 *Sketch History:* View up to 6 previously generated images (stored in browser).
* 📥 *Downloadable Art:* Easily download your AI-generated images.
* 🌗 *Light/Dark Mode Toggle:* Choose a theme that suits your environment.

---

## 🛠️ Tech Stack

| Technology       | Purpose                    |
| ---------------- | -------------------------- |
| HTML, CSS, JS    | Frontend                   |
| Flask            | Backend framework (Python) |
| Hugging Face API | AI image generation        |
| Web Speech API   | Voice-to-text recognition  |
| localStorage     | Save image history locally |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.7+
* A Hugging Face API token
* Internet connection

### Installation

1. *Clone the repository:*

   bash
   git clone https://github.com/your-username/voice-to-sketch-ai.git
   cd voice-to-sketch-ai
   

2. *Install dependencies:*

   bash
   pip install flask requests
   

3. *Set your Hugging Face token in app.py:*

   python
   HUGGINGFACE_API_TOKEN = "your_token_here"
   

4. *Run the app:*

   bash
   python app.py
   

5. *Open in browser:*

   
   http://127.0.0.1:5000
   

---

## 📸 Preview

![Demo Screenshot](link-to-screenshot-or-gif-if-you-have-one)

---

## 🧠 Example Prompts

* “a castle floating in the clouds”
* “robot painting a sunset”
* “a kitten flying a rocket ship”

---

## 📂 Folder Structure


/voice-to-sketch-ai
│
├── templates/
│   └── index.html       # Frontend UI
├── static/              # Optional if using CSS/JS assets
├── app.py               # Flask backend
└── README.md


---

## 📝 License

This project is licensed under the *MIT License*.

---

## 🙌 Acknowledgements

* [Hugging Face](https://huggingface.co/) for their Stable Diffusion API
* [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
* [Flask](https://flask.palletsprojects.com/) for backend framework
