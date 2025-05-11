
# 🤖 AI Agent using Google Gemini GenAI

This project is an experimental **AI Agent** powered by **Google's Gemini GenAI** and the **LangChain** ecosystem. The goal is to build a flexible, interactive assistant that can process user input, invoke tools, and respond intelligently—all through conversational AI.

---

## 🚧 Project Status: In Progress

> ⚠️ This project is currently under active development.

The core functionalities are in place, and future enhancements are planned to significantly expand the agent’s capabilities:

### 🧭 Planned Features (Not guaranteed due to a busy schedule)
- 🖥️ **Add a graphical UI** for the chat experience.  
- 🧰 **Incorporate additional tools** to handle more complex tasks.  
- 🧠 **Fine-tune the model** for higher contextual accuracy.  
- 🎙️ **Introduce voice interaction** for hands-free communication.

---

## 📦 Dependencies

### ✅ Python Version
Requires **Python 3.13+**

### 📚 Required Libraries
```toml
requires-python = ">=3.13"
dependencies = [
    "google-generativeai>=0.8.5",
    "langchain>=0.3.25",
    "langchain-google-genai>=2.0.10",
    "langchain-openai>=0.3.16",
    "langgraph>=0.4.3",
    "python-dotenv>=1.1.0"
]
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set up environment variables
Create a `.env` file and add your Gemini API key and any other required environment variables:
```
GOOGLE_API_KEY=your_key_here
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the project
```bash
python main.py
```

---

## 💬 What It Can Do

Once running, your AI agent can:

- Respond to user input intelligently using Gemini
- Use custom tools such as a calculator
- Be extended easily with new tool definitions
- Provide streamed conversational output

---

## 💡 Inspiration

This project was inspired by the [**Tech With Tim**](https://www.youtube.com/@TechWithTim) YouTube channel. Huge thanks to Tim for his educational and practical AI content!

---

## 🤝 Contributions

Contributions, feedback, and ideas are welcome. Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
