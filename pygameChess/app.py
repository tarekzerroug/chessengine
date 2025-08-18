from flask import Flask, render_template

print(__name__)
app = Flask(__name__)


@app.route('/')
def index():
   
    return render_template('index.html')


if __name__ == '__main__':

    # The app will be accessible at http://127.0.0.1:5000/
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while running the app: {e}")
