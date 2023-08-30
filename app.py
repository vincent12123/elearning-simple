from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Daftar soal quiz
quiz_data = [
    {
        'question': 'Apa ibukota Indonesia?',
        'options': ['Jakarta', 'Bandung', 'Surabaya'],
        'answer': 'Jakarta'
    },
    {
        'question': '5 + 5 = ?',
        'options': ['5', '10', '20'],
        'answer': '10'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_quiz')
def start_quiz():
    session['score'] = 0
    session['question_index'] = 0
    return render_template('quiz.html', quiz_data=quiz_data, question_index=session['question_index'])

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form.get('option')
    correct_answer = quiz_data[session['question_index']]['answer']
    
    if user_answer == correct_answer:
        session['score'] += 1
    
    session['question_index'] += 1
    
    if session['question_index'] < len(quiz_data):
        return render_template('quiz.html', quiz_data=quiz_data, question_index=session['question_index'])
    else:
        return f"Quiz selesai. Skor Anda: {session['score']}"

if __name__ == "__main__":
    app.run(debug=True)
