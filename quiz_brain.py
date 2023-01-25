class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < (len(self.question_list))

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False) : ").title()
        self.check_answer(q_answer, current_question)

    def check_answer(self, q_answer, current_question):
        if q_answer == current_question.answer:
            print("You are Right!")
            self.score += 1

        else:
            print("You are Wrong!")
        print(f"The Correct Answer Was : {current_question.answer}")
        self.q_score()

    def q_score(self):
        print(f"Your Score Was : {self.score}/{self.question_number} \n")
