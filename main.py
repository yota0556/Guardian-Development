from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False)