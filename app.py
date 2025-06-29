from flask import Flask, render_template, request, jsonify
import requests
import base64

app = Flask(__name__)

# ✅ Your Hugging Face token
HUGGINGFACE_API_TOKEN ="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"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/draw", methods=["POST"])
def draw():
    data = request.get_json()
    command = data.get("command", "")
    style_prefix = data.get("style", "black and white pencil sketch of")

    if not command:
        return jsonify({"status": "error", "message": "No voice command received"})

    prompt = f"{style_prefix} {command}"

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt}, stream=True)

        if response.status_code == 404:
            return jsonify({"status": "error", "message": "❌ Model not found – use exact name: stabilityai/stable-diffusion-xl-base-1.0"})
        elif response.status_code == 401:
            return jsonify({"status": "error", "message": "❌ Invalid Hugging Face token (401)"})

        if response.status_code != 200:
            return jsonify({"status": "error", "message": f"❌ Error {response.status_code}: {response.text}"})

        image_data = response.content
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        return jsonify({"status": "ok", "image": f"data:image/png;base64,{image_base64}"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
