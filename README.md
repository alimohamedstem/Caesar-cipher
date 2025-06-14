# 🔐 Caesar Cipher - Encrypt & Decrypt Text

![License](https://img.shields.io/badge/License-MIT-blue.svg)  
![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)

A simple Python script that encrypts and decrypts messages using the **Caesar Cipher** — one of the oldest encryption techniques in history.

---

## 🖼️ Preview

![Trial Screenshot](https://github.com/alimohamedstem/Caesar-cipher/blob/main/Trial.png)

---

## 📌 Features

- 🔄 **Encrypt** lowercase messages with a shift from 1 to 25  
- 🔓 **Decrypt** Caesar-encrypted text  
- 🧠 Keeps spaces intact  
- 🔁 Retry option on wrong input  
- 🐍 Written in pure Python — no extra libraries needed

---

## 🧠 How It Works

The Caesar Cipher shifts each letter in the alphabet by a fixed amount.

For example, with a shift of **3**:

```
a → d  
b → e  
c → f  
...  
x → a  
y → b  
z → c
```

Only lowercase letters are supported; spaces are preserved.

---

## 🧪 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/alimohamedstem/Caesar-cipher.git
   cd Caesar-cipher
   ```

2. **Run the script**
   ```bash
   python caesar_cipher.py
   ```

3. **Follow the prompts**
   - Enter the message
   - Choose `encrypt` or `decrypt`
   - Provide a shift number between 1 and 25

---

## ✅ Example Run

```text
The text: 
stem students
encrypt or decrypt 
encrypt
The shift number from 1 to 25: 
5
xyrq xyzwjyrx
```

---

## 🗂 Project Structure

```
📁 Caesar-cipher/
├── caesar_cipher.py       # Main Python script
├── trial.png              # Screenshot or banner
└── README.md              # Project documentation
```

---

## 🚀 Future Improvements

- 🔡 Support uppercase letters and punctuation  
- 🖥️ Add a GUI with Tkinter or a web interface with Flask  
- 💾 Save results to a text file  
- 📋 Copy output to clipboard automatically  

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed with 💙 by [Ali Mohamed](https://github.com/alimohamedstem)

> If you like this project, ⭐ star the repo and share it with others!
