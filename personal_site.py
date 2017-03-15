from flask import Flask, Markup, render_template
from flask_flatpages import FlatPages
import markdown
import os
import sys

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

@app.route('/')
def index():
    title = "Home"
    content = 'pages/index.md'
    list_of_pages = [p for p in pages]
    content = Markup(markdown.markdown(open('./index.md', 'r').read()))
    return render_template('index.html', title=title, list_of_pages=list_of_pages, content=content)

def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/<path>/')
def page(path):
    list_of_pages = [p for p in pages]
    print list_of_pages
    from pprint import pprint
    pprint (vars(list_of_pages[2]))
    page = pages.get_or_404(path).html
    content = Markup(markdown.markdown(open('./pages/'+ str(path) + ".md", 'r').read()))
    content = content.split('<!----->')[1]
    return render_template('index.html', content=content, title=str(path).capitalize(),
                           list_of_pages=list_of_pages)

if __name__ == '__main__':
    app.run(debug=True)
