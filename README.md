###### This tutorial assumes you have a basic knowledge of Python (syntax and built in functions), running on mac, basic understanding of command line, and a basic understanding of how the web works (don't worry, we'll go over some foundation). 
# Intro to General Webdev
## Review
### What is a web server?

Simply said, a web server is a program that's running on a machine that is waiting for a web request. It can process requests and issue responses using HTTP. HTTP is a protocol used to distribute information on the web. 

Here's a very simple example, if you open `https://www.google.com` on your preferred web browser, it will send a `request` to Google's web server, look for it's  `index.html`  and returns the `<html> blah blah blah </html>` back to the browser to be rendered on the user's browser.

_* *In case this sparks your interest, yes, this is naively how DDOSing works—making a bunch of requests to a web server to slow it down or render it unusable* *_

Some popular web servers are [Apache](https://httpd.apache.org/) and [nginx](https://www.nginx.com/resources/wiki/).

## Two major Python web frameworks: Django and Flask
* [**Flask:**](http://flask.pocoo.org/) Microframework 
    * Lightweight
    * Extensions available to customize your framework
    * "Hands on the wire" approach
    * Can scale and be used in production (Ex. [Pinterest](https://www.quora.com/What-challenges-has-Pinterest-encountered-with-Flask) and [Twilio](https://www.twilio.com/docs/quickstart/python/sms/hello-monkey))
* [**Django:**](https://www.djangoproject.com/) Full framework aka _"batteries included"_
    * Comes with a default set up ("boilerplate") and collection of modules that are ready to use
        * Ex. User authentication, management panel, forms, upload files, etc
    * Can scale and be used in production (Ex. [Spotify](https://labs.spotify.com/2013/03/20/how-we-use-python-at-spotify/), [Instagram](https://stackoverflow.com/questions/12763792/how-does-instagram-use-django), [The Washington Post](https://www.djangoproject.com/weblog/2005/dec/08/congvotes/))
# "Live" Coding
## Virtual Environvment
*   [virtualenv](https://virtualenv.pypa.io/en/stable/#introduction)
    * A tool that allows the user to create multiple isolated Python environments on one machine. _(e.g. system uses v2.6, one app uses v3.5 and another v2.7.)_

      ###### Your directory should look something like this if you named your virtualenv (venv)

      ![file_directory](https://i.imgur.com/jGEWzWE.png)

    * Keeps different project environments isolated and contained

      * _Note: Make sure if you create a `.gitignore` file by using the command `touch .gitignore`, and adding **venv** and **secret** (for your secret key(s)) to avoid checking in your virtualenv and secret key(s) into the repo by adding these two lines to `.gitignore`._ 

        ```basic
        *venv*
        *secret*
        ```

*   **For installation instructions and setting up virtualenv:** http://flask.pocoo.org/docs/0.12/installation/#installation 

  `pip install flask` installs all of flasks dependencies and the default templating language. (There are many others to choose from.)

    ```basic
        (venv) ruru [~/Desktop/flask_presentation] pip install flask
        Collecting flask
          Downloading Flask-0.12-py2.py3-none-any.whl (82kB)
            100% |████████████████████████████████| 92kB 541kB/s 
        Collecting itsdangerous>=0.21 (from flask)
          Downloading itsdangerous-0.24.tar.gz (46kB)
          100% |████████████████████████████████| 51kB 3.4MB/s
        Collecting Werkzeug>=0.7 (from flask)
          Downloading Werkzeug-0.11.15-py2.py3-none-any.whl (307kB)
            100% |████████████████████████████████| 317kB 2.0MB/s
        Collecting Jinja2>=2.4 (from flask)
          Downloading Jinja2-2.9.5-py2.py3-none-any.whl (340kB)
            100% |████████████████████████████████| 348kB 2.4MB/s 
        Collecting click>=2.0 (from flask)
          Downloading click-6.7-py2.py3-none-any.whl (71kB)
            100% |████████████████████████████████| 71kB 7.1MB/s 
        Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->flask)
          Downloading MarkupSafe-0.23.tar.gz
        Building wheels for collected packages: itsdangerous, MarkupSafe
          Running setup.py bdist_wheel for itsdangerous ... done
          Stored in directory: /Users/Dragonair/Library/Caches/pip/wheels/fc/a8/66/24d655233c757e178d45dea2de22a04c6d92766abfb741129a
          Running setup.py bdist_wheel for MarkupSafe ... done
          Stored in directory: /Users/Dragonair/Library/Caches/pip/wheels/a3/fa/dc/0198eed9ad95489b8a4f45d14dd5d2aee3f8984e46862c5748
        Successfully built itsdangerous MarkupSafe
        Installing collected packages: itsdangerous, Werkzeug, MarkupSafe, Jinja2, click, flask
        Successfully installed Jinja2-2.9.5 MarkupSafe-0.23 Werkzeug-0.11.15 click-6.7 flask-0.12 itsdangerous-0.24
    ```

## What is Flask
Flask is a highly flexible, small, simple, and elegant Python web framework. Generally, it is used with a templating framework, Jinja2 _(as mentioned above)_. 

For the purpose of this tutorial, we will start with the standard 'Hello World' tutorial from the official docs.

## Demo App: Hello World pt 1
[`Link: Hello World`](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application) 

Create an empty file with `touch server.py`.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

To run the app type in the command line:

```basic
> export FLASK_APP=server.py
> flask run
```

_*Note: `export FLASK_APP=server.py` creates an environment variable that only needs to written once. Some people opt to use environment variables instead of having a secrets file._

Result: 

```basic
 * Serving Flask app "server"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

In this instance, the flask server is now up and running on its default localhost:5000. Now, go to localhost:5000 in your preferred browser and you'll see 'Hello World' in plain text.

Now, let's break it down line-by-line to understand what's going on within those few lines of code better. Since real world applications are more object-orientated and split into pieces, we can refactor the code after we solidify our understanding. 

Import necessary library:

```python
from flask import Flask
```

Instantiate a Flask app:

```python
app = Flask(__name__)
```

Program the default **route** to 'Hello World':

```python
@app.route('/')
def hello_world():
    return 'Hello, World!'
```

## Routing

In web development, most modern web frameworks use a routing technique to help a user easily reference URL's. `@app.route('')` is a [**decorator**](https://wiki.python.org/moin/PythonDecorators) that binds the URL to a function. 

When a user goes to a URL such as `http://www.sampleapp.com/signup'` it would find the decorator `@app.route('/signup')` in the `server.py` file and return the function associated to it. 

Our current 'Hello World' text from `localhost:5000` comes from this function `def hello_world():` returning the string `'Hello,World!'` which would then be rendered into the web browser. 

## Templating with Jinja2

### What is templating?

Templating is a way to represent data in different forms. The purpose of them is to reduce the amount of physical changes needed to change output (normally HTML) and reduce the amount of time spent on creating redundant code. Basic data manipulation is possible within templates such as traversing through lists forwards and backwards, capitalizing text, looping with for loops, etc. 

### What is [Jinja2](http://jinja.pocoo.org/)?

It the most popular and fully featured template engine for Python. It is the default templating engine for Flask (same creator), and, although, it is not the default templating engine used for Django, it is still an option. 

Here's a sample:

````python
{% extends "layout.html" %}
{% block content %}
  <h3> This is the start of my child template</h3>
  <br>
  <p>My string: {{my_string}}</p>
  <p>Value from the list: {{my_list[3]}}</p>
  <p>Loop through the list:</p>
  <ul>
    {% for n in my_list %}
    <li>{{n}}</li>
    {% endfor %}
  </ul>
  {% endblock %}
{% endblock %}
````

`extends` means that we will inject our content into an existing template, `layout.html` in this case. The portion that's unique to this particular HTML page is the content within `block content` and `end block`. 

Variables can be passed from view functions to the template with the `render_template` function and the double curly braces  are used to "bind" those values (aka, dynamically display).

In our 'Hello World', we can write a function and return a variable along with a template by importing the module `render_template`. 

For example:

```python
@app.route('/')
def hello_world():
    user = request.args.get('person')
    return render_template('index.html', user=name)
```

Broken down line-by-line:

This searches the submitted `<form>` values for one called `person` using the `request` module (can also be imported along with `render_template`) and binds it to the variable `user`.

```python
 user = request.args.get('person')
```

Here, we use the function `render_template`  to render the `index.html` template, and pass our local variable `name` to the template as variable  `user` (so that we can do `{{ user }}`.

```python
return render_template('index.html', user=name)
```

`{{my_list[3]}}` looks in the list `my_list` and replaces it with the contents of the 4th item in the list. 

```python
{% for n in my_list %}
    <li>{{n}}</li>
{% endfor %}
```

This is a Jinja2 `for` loop. Amazing, right? A `for` loop INSIDE of HTML. Unfortunately, `while` loops are not supported. 

## Demo App: Hello World pt 2

With routing and templating in mind, let's make this 'Hello World' more interesting. 

At this time, go ahead and quit out of your previous instance of the 'Hello World' app by pressing `CTRL+C`.

First, let's bind the application name to a variable and turn on the debugger by adding these two lines under the `@app.route('/')` route.

The `server.py` file should look like this:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
```

 _* *For a deeper understanding of what `__name__ == "__main__":` does, [click here.](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)*_

In the command line, instead of:

```basic
> export FLASK_APP=server.py
> flask run
```

Type in:

```basic
> python server.py
```

Surprise! It now instantly spins up the server. 

We'll now start adding in some HTML. Create a directory called `templates` using `mkdir templates` in the command line, `cd templates` to enter that directory and create a file called `index.html` in templates using `touch index.html`. 

In `index.html`, add in this code for a simple form:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Who are you?</title>
</head>
<body>
    <form action="/welcome">
        <label>What's your name?
            <input type="text" name="person">
        </label>
        <input type="submit">
    </form>
</body>
</html>
```

And, in `server.py`, add `render_template` to import's and, and create a new function called `greeting_generator`.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/greetings')
def greeting_generator():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
```

In the command line, type `cd ..` to go back to the root directory of the app and run the server using `python server.py`.

Refresh or reopen your `localhost:5000` browser window and you should see:

![greeting_form](https://i.imgur.com/n1yfbMb.png)

We have a form that collects a user input (the name) when we click on `Submit`, but that form doesn't go anywhere yet. However, the URL has changed to:

`http://localhost:5000/welcome?person=Frances`

Let's add `request` to imports, and create another route `welcome` that greets the person. _*Note: It is possible to do this within one function, but for the purpose of this tutorial we will do this separately._

The `server.py` should look like this:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/greetings')
def greeting_generator():
    return render_template("index.html")


@app.route('/welcome')
def greeting():
    user = request.args.get("person")
    return render_template("greeting.html", name=user)


if __name__ == "__main__":
    app.run(debug=True)
```

Also, let's create another html template called `greetings.html`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome!</title>
</head>
<body>
    Welcome, {{ name }}.
</body>
</html>
```

Now, go ahead and run the server again with `python sever.py`.

Voila! You should now see something like this:

![working_form](https://i.imgur.com/XWEtHEq.gif)

Sweet, we now have super simple app that collects information and outputs it. _*Note: In the future, we can incorporate various databases and utilize `flask-sqlalchemy`._

# My Dev Environment and Tools

* Sublime Text 3
  * Theme: [Afterglow.sublime-theme](https://github.com/YabataDesign/afterglow-theme)
  * Some of the extensions I use: 
    * [Python PEP8](https://packagecontrol.io/packages/Python%20PEP8%20Autoformat)
    * [Wakatime](https://packagecontrol.io/packages/WakaTime)
    * [HTML CSS JS Prettify](https://packagecontrol.io/packages/HTML-CSS-JS%20Prettify)
* Command Line
  * Theme: [Solarized Dark Yosemite](https://github.com/altercation/solarized)
* GIFS
  * [Gifox](http://gifox.io/)
  * [RecordIt](http://recordit.co/)
* Presentation
  * [RevealJS](https://github.com/hakimel/reveal.js)

# Extra Reading

* [Flask vs DJango](https://www.codementor.io/garethdwyer/flask-vs-django-why-flask-might-be-better-4xs7mdf8v)
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Flask Mega-Tutorail _(dated 2012_)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

# Next Up

Please let me know if you have any questions, suggestions, and if you'd be intersted in diving deeper in Flask in an extended session.

**Slack:** @frances.liu

**Email:** frances.liu@teradata.com

**Possible topics:**

* Making a Slackbot with Flask

* Making a Twilio app with Flask

* Making a Flask blog

* Making a Flask API

* Making a TweeterBot with Flask

* Django Hello World

* Django Blog

* Django vs Flask (side by side)

  _**Open to other suggestions_**
