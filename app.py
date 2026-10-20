# CS50x Final Project: LexiBoost - Vocabulary App
# Name: Siraj Ahmed
# City, Country: Rawalpindi, Pakistan
# Date: September 2026
# AI Citation: AI assistance was used for initial Flask layout structuring.

from flask import Flask, render_template_string
import urllib.parse

app = Flask(__name__)

VOCAB_DATA = [
    {
        "word": "Eloquent",
        "pronunciation": "/ˈɛləkwənt/",
        "meaning": "Fluent or persuasive in speaking or writing.",
        "example": "She gave an eloquent speech at the ceremony."
    },
    {
        "word": "Resilient",
        "pronunciation": "/rɪˈzɪliənt/",
        "meaning": "Able to recover quickly from difficult conditions.",
        "example": "He is resilient enough to bounce back from failure."
    },
    {
        "word": "Meticulous",
        "pronunciation": "/mɪˈtɪkjələs/",
        "meaning": "Showing great attention to detail; very careful.",
        "example": "He was meticulous about keeping his study notes clean."
    },
    {
        "word": "Pragmatic",
        "pronunciation": "/præɡˈmætɪk/",
        "meaning": "Dealing with things sensibly and realistically.",
        "example": "We need a pragmatic solution to solve this problem."
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LexiBoost - Vocabulary App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f4f6f9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .mobile-card { max-width: 400px; margin: 40px auto; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); background: #ffffff; padding: 25px; }
        .word-title { color: #3f51b5; font-weight: 700; }
        .btn-whatsapp { background-color: #25D366; color: white; font-weight: 600; border-radius: 10px; }
        .btn-whatsapp:hover { background-color: #1eb854; color: white; }
    </style>
</head>
<body>
    <div class="container text-center">
        <div class="mobile-card">
            <h2 class="mb-1">LexiBoost 🚀</h2>
            <p class="text-muted small mb-4">Daily Vocabulary Improvement App</p>

            <div id="card-content" class="p-3 bg-light rounded-3 mb-3 border">
                <h3 id="word" class="word-title mb-1"></h3>
                <p id="pron" class="text-secondary fst-italic mb-3"></p>
                <hr>
                <p class="text-start mb-1"><strong>Meaning:</strong></p>
                <p id="meaning" class="text-start text-dark mb-3"></p>
                <p class="text-start mb-1"><strong>Example:</strong></p>
                <p id="example" class="text-start text-muted fst-italic mb-0"></p>
            </div>

            <div class="d-flex justify-content-between mb-3">
                <button class="btn btn-outline-primary" onclick="prevCard()">Previous</button>
                <button class="btn btn-primary" onclick="nextCard()">Next</button>
            </div>

            <button class="btn btn-whatsapp w-100 py-2 mb-2" onclick="shareWhatsApp()">Share to WhatsApp Status 📲</button>
            <button class="btn btn-outline-warning w-100 py-2" onclick="bookmarkWord()">Bookmark Word ⭐</button>
        </div>
    </div>

    <script>
        const vocabData = {{ vocab | tojson }};
        let currentIndex = 0;

        function updateCard() {
            const item = vocabData[currentIndex];
            document.getElementById('word').innerText = item.word;
            document.getElementById('pron').innerText = item.pronunciation;
            document.getElementById('meaning').innerText = item.meaning;
            document.getElementById('example').innerText = `"${item.example}"`;
        }

        function nextCard() {
            currentIndex = (currentIndex + 1) % vocabData.length;
            updateCard();
        }

        function prevCard() {
            currentIndex = (currentIndex - 1 + vocabData.length) % vocabData.length;
            updateCard();
        }

        function bookmarkWord() {
            alert(`'${vocabData[currentIndex].word}' has been bookmarked!`);
        }

        function shareWhatsApp() {
            const item = vocabData[currentIndex];
            const text = `🌟 *Word of the Day: ${item.word}*\\n🗣️ ${item.pronunciation}\\n💡 *Meaning:* ${item.meaning}\\n✍️ *Example:* ${item.example}\\n\\nLearned via LexiBoost App! 🚀`;
            window.open(`https://wa.me/?text=${encodeURIComponent(text)}`, '_blank');
        }

        updateCard();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, vocab=VOCAB_DATA)

if __name__ == '__main__':
    app.run(debug=True)
