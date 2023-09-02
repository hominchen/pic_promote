from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        total_prompt = request.form.getlist('mycheckbox')
        return render_template('index.html',
                total_prompt=total_prompt)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)