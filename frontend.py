from flask import Flask, render_template
from flask_cors import CORS  # CORS 허용을 위한 모듈 추가

app = Flask(__name__, template_folder="templates")  # templates 폴더 설정
CORS(app)  # 모든 도메인에서의 접근을 허용

@app.route("/")
def home():
    return render_template("connect.html")

@app.route("/index")  # ✅ index.html 라우트 추가
def index():
    return render_template("index.html")

if __name__ == "__main__":  # 메인 함수
    app.run(host="0.0.0.0", port=5000, debug=True)  # Flask 서버 실행
