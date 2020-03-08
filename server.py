from flask import Flask, request, render_template
from gensim.summarization.summarizer import summarize
import spacy

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/summarize', methods=["POST"])
def get_summary():
  if request.method == "POST":
    submission = request.form['submission']
    summary = summarize(submission).split('.')
    
    nlp = spacy.load("en_core_web_sm")
    document = nlp(submission)
    
    people = []
    for entity in document.ents:
      print(entity.label)
      if entity.label == 380:
        people.append(entity.text)
    
    return render_template('summary.html', 
                           summary=summary,
                           people=set(people))

if __name__ == '__main__':
  app.run(debug=True)