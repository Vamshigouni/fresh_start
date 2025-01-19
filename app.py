from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# First Page
@app.route('/')
def first_page():
    return render_template('first.html')

# Second Page
@app.route('/second')
def second_page():
    return render_template('second.html')

# Third Page
@app.route('/third', methods=['GET', 'POST'])
def third_page():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == 'yes':
            return "Thank you! ❤️"
        else:
            return "I'm really sorry. 😔"
    return render_template('third.html')

if __name__ == '__main__':
    app.run(debug=True)
