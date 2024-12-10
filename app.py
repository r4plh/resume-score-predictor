from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    uploaded_files = request.files.getlist('resume_folder[]')
    for file in uploaded_files:
        if file.filename.endswith('.pdf'):
            filename = os.path.join('uploads', file.filename)
            file.save(filename)
    job_description = request.form['job_description']
    with open('uploads/job_description.txt', 'w') as f:
        f.write(job_description)
    data = {
        'duddumaheshchandra@gmail.com': 52.0, 
        'boddapatikarthik12@gmail.com': 47.0, 
        'ranjith.kumar.kn26@gmail.com': 67.0, 
        'kshitij.jobs02@gmail.com': 56.0, 
        'vedantmahalle21@gmail.com': 61.0, 
        'ahamedwasif07@gmail.com': 73.0, 
        'narendramall.iitkgp@gmail.com': 55.0, 
        'akshat.agarwal0311@gmail.com': 49.0, 
        'sauravbittoo8@gmail.com': 42.0, 
        'vineethvooradi9@gmail.com': 48.0, 
        'mk6991778@gmail.com': 58.0, 
        'vempati.bindumadhavi@gmail.com': 58.0, 
        'a.nasir0001@gmail.com': 64.0, 
        'manasikhillare0011@gmail.com': 49.0, 
        'tamylv.pb@gmail.com': 49.0, 
        'iamvishalsharma.vs@gmail.com': 49.0, 
        'ramyashree1301@gmail.com': 59.0, 
        'sunnydhoke22@gmail.com': 55.0, 
        'ashfaqsyedn@gmail.com': 59.0, 
        'adityarajtheonly@gmail.com': 48.0, 
        'anupdogrial@gmail.com': 52.0, 
        'aarushgupta212@gmail.com': 52.0
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
