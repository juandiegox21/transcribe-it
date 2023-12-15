from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)

@app.route("/transcribe")
def transcribe():
    model = whisper.load_model("medium")
    result = model.transcribe("audio.wav")

    return jsonify({
        "transcript": result["text"],
        "segments": result.get("segments", []) 
    })

if __name__ == '__main__':
    app.run(debug=True)