
```markdown
# 🎯 Tag Generator (NLP-based)

This is an NLP-powered YouTube tag generation tool built using **Flask**, **Transformers**, and **pretrained Hugging Face models**. The app generates high-quality video tags from raw text input, using models fine-tuned for text-to-tag tasks.

---

## 🚀 Features

- 🔥 Supports two different tag-generation models:
  - [`fabiochiu/t5-base-tag-generation`](https://huggingface.co/fabiochiu/t5-base-tag-generation)
  - [`efederici/text2tags`](https://huggingface.co/efederici/text2tags)
- 🧠 Transformer-based predictions (via Hugging Face Transformers)
- 🌐 RESTful API using Flask
- 🔒 CORS enabled for frontend integration
- ✅ Easily configurable using `.env`

---

## 📁 Project Structure

```

YouTube-Tag-Generation/
│
├── config/                       # Environment config loader
│   └── config.py
│
├── tag\_generation/
│   ├── logger/                   # Logging setup
│   │   └── **init**.py
│   ├── models\_interface/         # Model interaction scripts
│   │   ├── t5\_tags.py
│   │   └── text\_2\_tags.py
│   └── src/
│       └── main.py              # Flask app entry
│
├── models/                      # Cloned models (see below)
│   ├── t5-base-tag-generation/
│   └── text2tags/
│
├── run.py                       # Main script to launch the app
├── requirements.txt             # Python dependencies
└── .env                         # Environment configuration

````

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Maharaj7809/Tag-Generation.git
cd Tag-Generation
````

### 2️⃣ Clone the Required Models

```bash
# Clone T5 Tag Generator Model
git clone https://huggingface.co/fabiochiu/t5-base-tag-generation models/t5-base-tag-generation

# Clone Text2Tags Model
git clone https://huggingface.co/efederici/text2tags models/text2tags
```

### 3️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # On macOS/Linux
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Create the `.env` file

Create a `.env` file in the project root with the following content:

```env
MAX_NEW_TOKEN=32
NUM_BEAMS=4
T5_TAGS_MODEL_PATH=models/t5-base-tag-generation/
TEXT_TO_TAGS_MODEL_PATH=models/text2tags/
```

> ⚠️ Make sure the variable names in `.env` exactly match those used in your `config.py`. For example, if your code uses `MAX_NEW_TOKENS` (plural), update the `.env` accordingly.

### 6️⃣ Run the Application

```bash
python run.py
```

The Flask API will start running locally (usually at `http://127.0.0.1:5000`).

---

## ✅ API Usage

### Endpoint: `/generate_tags`

#### Request (POST):

```json
{
  "text": "Your YouTube video title or description",
  "model": "t5"  // or "text2tags"
}
```

#### Response:

```json
{
  "tags": ["AI", "Machine Learning", "NLP"]
}
```

---

## 📦 Dependencies

* `Flask`
* `flask-cors`
* `transformers`
* `torch`
* `nltk`
* `python-dotenv`
* `scikit-learn`
* `pandas`
* `numpy`

Install all dependencies via:

```bash
pip install -r requirements.txt
```

---

