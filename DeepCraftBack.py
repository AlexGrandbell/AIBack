from flask import Flask, request, Response
import requests
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

AI_BASE_URL = "https://api.deepseek.com/chat/completions"
API_KEY = "替换成你的API密钥，需在DeepSeek官网购买"


def stream_deepseek_response(payload):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    with requests.post(AI_BASE_URL, json=payload, headers=headers, stream=True) as response:
        if response.status_code != 200:
            yield json.dumps({"error": f"服务器错误: {response.status_code}"}) + "\n"
            return

        for chunk in response.iter_lines():
            if chunk:
                try:
                    decoded_line = chunk.decode("utf-8").replace("data: ", "")
                    if decoded_line.strip() == "[DONE]":
                        break
                    parsed = json.loads(decoded_line)
                    yield f"data: {json.dumps(parsed)}\n\n"  # 按 SSE 格式返回数据
                except json.JSONDecodeError:
                    continue


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    payload = {
        "model": data.get("model", "deepseek-chat"),
        "messages": data["messages"],
        "frequency_penalty": data.get("frequency_penalty", 1.0),
        "stream": True,
    }
    return Response(stream_deepseek_response(payload), content_type="text/event-stream")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5110, debug=False, threaded=True)