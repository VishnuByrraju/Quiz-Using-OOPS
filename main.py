from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question = Question(i['question'], i['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You Have Completed The Quiz! \nYour Final Score Is {quiz.score}/{quiz.question_number}")

