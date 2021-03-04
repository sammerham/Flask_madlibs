from flask import Flask, render_template, request

# from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

# debug = DebugToolbarExtension(app)


@app.route("/")
def prompt():
    """ prompt user for words"""
    prompts = silly_story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def generateStory():
    """generate story from prompt inputs"""

    story = silly_story.generate(request.args)

    return render_template("story.html", story=story)