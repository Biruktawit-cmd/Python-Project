def display_welcome():
    """Display welcome message"""
    print("\n" + "="*60)
    print("WELCOME TO THE GENERAL KNOWLEDGE QUIZ".center(60))
    print("="*60)
    print("\nAnswer each multiple-choice question by entering A, B, C, or D")
    print("Good luck!\n")


def display_question(question_num, total_questions, question_data):
    """Display a single question with options"""
    print("\n" + "-"*60)
    print(f"Question {question_num}/{total_questions}")
    print("-"*60)
    print(f"\n{question_data['question']}\n")
    
    for option, text in question_data['options'].items():
        print(f"  {option}. {text}")


def get_answer():
    """Get and validate user's answer"""
    while True:
        answer = input("\nYour answer (A/B/C/D): ").upper().strip()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")


def display_result(is_correct):
    """Display immediate feedback"""
    if is_correct:
        print("✓ Correct!")
    else:
        print("✗ Incorrect!")


def display_final_results(score, total, wrong_answers, quiz_questions):
    """Display final score and review wrong answers"""
    print("\n" + "="*60)
    print("QUIZ COMPLETED!".center(60))
    print("="*60)
    
    # Display score
    percentage = (score / total) * 100
    print(f"\nYour Score: {score}/{total} ({percentage:.1f}%)")
    
    # Performance message
    if percentage >= 90:
        print("Outstanding! Excellent work! 🌟")
    elif percentage >= 70:
        print("Great job! Well done! 👏")
    elif percentage >= 50:
        print("Good effort! Keep learning! 📚")
    else:
        print("Keep practicing! You'll improve! 💪")
    
    # Review wrong answers
    if wrong_answers:
        print("\n" + "="*60)
        print("REVIEW - Questions You Got Wrong".center(60))
        print("="*60)
        
        for wrong in wrong_answers:
            q_num = wrong['question_num']
            q_data = quiz_questions[q_num - 1]
            
            print(f"\n{'-'*60}")
            print(f"Question {q_num}: {q_data['question']}")
            print(f"\nYour answer: {wrong['user_answer']}. {q_data['options'][wrong['user_answer']]}")
            print(f"Correct answer: {q_data['correct']}. {q_data['options'][q_data['correct']]}")
            
            if 'explanation' in q_data:
                print(f"\nExplanation: {q_data['explanation']}")
    else:
        print("\nPerfect score! You got all questions correct! 🎉")
    
    print("\n" + "="*60)


def main():
    # Quiz questions database
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": {
                "A": "London",
                "B": "Berlin",
                "C": "Paris",
                "D": "Madrid"
            },
            "correct": "C",
            "explanation": "Paris has been the capital of France since the 12th century."
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": {
                "A": "Venus",
                "B": "Mars",
                "C": "Jupiter",
                "D": "Saturn"
            },
            "correct": "B",
            "explanation": "Mars appears red due to iron oxide (rust) on its surface."
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": {
                "A": "Atlantic Ocean",
                "B": "Indian Ocean",
                "C": "Arctic Ocean",
                "D": "Pacific Ocean"
            },
            "correct": "D",
            "explanation": "The Pacific Ocean covers about 46% of Earth's water surface."
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": {
                "A": "Vincent van Gogh",
                "B": "Leonardo da Vinci",
                "C": "Pablo Picasso",
                "D": "Michelangelo"
            },
            "correct": "B",
            "explanation": "Leonardo da Vinci painted the Mona Lisa between 1503 and 1519."
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": {
                "A": "Go",
                "B": "Gd",
                "C": "Au",
                "D": "Ag"
            },
            "correct": "C",
            "explanation": "Au comes from the Latin word 'aurum' meaning gold."
        },
        {
            "question": "How many continents are there?",
            "options": {
                "A": "5",
                "B": "6",
                "C": "7",
                "D": "8"
            },
            "correct": "C",
            "explanation": "The seven continents are: Africa, Antarctica, Asia, Australia, Europe, North America, and South America."
        },
        {
            "question": "What is the smallest prime number?",
            "options": {
                "A": "0",
                "B": "1",
                "C": "2",
                "D": "3"
            },
            "correct": "C",
            "explanation": "2 is the smallest and only even prime number."
        },
        {
            "question": "Which programming language is known as the 'language of the web'?",
            "options": {
                "A": "Python",
                "B": "Java",
                "C": "JavaScript",
                "D": "C++"
            },
            "correct": "C",
            "explanation": "JavaScript runs in web browsers and powers interactive web pages."
        },
        {
            "question": "What year did World War II end?",
            "options": {
                "A": "1943",
                "B": "1944",
                "C": "1945",
                "D": "1946"
            },
            "correct": "C",
            "explanation": "World War II ended in 1945 with Japan's surrender in September."
        },
        {
            "question": "What is the speed of light in vacuum (approximately)?",
            "options": {
                "A": "300,000 km/s",
                "B": "150,000 km/s",
                "C": "500,000 km/s",
                "D": "1,000,000 km/s"
            },
            "correct": "A",
            "explanation": "Light travels at approximately 299,792 km/s in a vacuum."
        }
    ]
    
    # Initialize game variables
    score = 0
    total_questions = len(quiz_questions)
    wrong_answers = []
    
    # Display welcome message
    display_welcome()
    
    # Ask each question
    for i, question_data in enumerate(quiz_questions, 1):
        # Display question
        display_question(i, total_questions, question_data)
        
        # Get user's answer
        user_answer = get_answer()
        
        # Check if correct
        is_correct = user_answer == question_data['correct']
        
        if is_correct:
            score += 1
            display_result(True)
        else:
            display_result(False)
            wrong_answers.append({
                'question_num': i,
                'user_answer': user_answer
            })
    
    # Display final results
    display_final_results(score, total_questions, wrong_answers, quiz_questions)


if __name__ == "__main__":
    main()
