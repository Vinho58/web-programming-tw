# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Variables to pass to the HTML template
    title = "My Profile"
    name = "Kevin Friedl"
    description = "This semester I study at Taipei Tech as an exchange student. Back home in Germany I study Business Informatics. In this class I learn how to build websites. First we had HTML and CSS. Then came JavaScript. Now I build my first web app with Python and Flask. After the semester I want to travel more in Asia before I start my bachelor thesis."
    quote = "Taipei Tech"
    hobbies = [
        ["Football", "My favorite sport. I play with my friends and watch a lot of games."],
        ["Money", "I like to learn how to save money and how investing works."],
        ["Holiday", "When I have time off, I go on holiday and relax."],
        ["Travel", "I love to see new cities and countries."]
    ]
    skills = ["HTML", "CSS", "JavaScript", "Python", "Flask"]

    # Render the template and pass the variables
    return render_template('index.html', title=title, name=name, description=description, quote=quote, hobbies=hobbies, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
