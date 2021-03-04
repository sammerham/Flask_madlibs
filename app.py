from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# debug = DebugToolbarExtension(app)



@app.route('/')
def prompt():
    """ prompt user for words"""
    prompts = silly_story.prompts
    print(prompts)
    return render_template("questions.html", prompts=prompts)

@app.route('/story.html')
