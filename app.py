# app.py

from flask import Flask, render_template, request
from issue_linker import IssueLinkerEnhanced

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('query', '')
    issue_linker = IssueLinkerEnhanced()
    df3 = issue_linker.find_related_issues(search_term)
    return render_template('search_results.html', table=df3.to_html())

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
