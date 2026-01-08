from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = ""

    if request.method == "POST":
        if "image" in request.files:
            image_file = request.files["image"]
            if image_file.filename != "":
                image_bytes = image_file.read()
                image = Image.open(io.BytesIO(image_bytes))
                # OCR (CPU)
                extracted_text = pytesseract.image_to_string(image)

    return render_template("index.html", text=extracted_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
