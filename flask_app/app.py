from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
@app.route('/')
@app.route('/')
def home():
    return '''
        <h1>Hello, World!</h1>
        <p><a href="/greet">Click here to go to the greeting form</a></p>
    '''

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    form_html = '''
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    '''
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = int(request.form['age'])
            return f"Hello, {name}! You are {age} years old."
        except ValueError:
            return "Invalid age input. Please enter a number."
    return render_template_string(form_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
