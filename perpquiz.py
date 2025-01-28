# Define questions as a list of dictionaries
questions = [
    {"Question": "What is the capital of Kenya?", 
     "Choices": ["A. Dodoma", "B. Nairobi", "C. Algiers", "D. Mogadishu"],
     "answer": "B"},

    {"Question": "What is the capital of Eritrea?", 
     "Choices": ["A. Bujumbura", "B. Addis Ababa", "C. Asmara", "D. Ouagadougou"],
     "answer": "C"},  

    {"Question": "What is the capital of Mali?",
     "Choices": ["A. Harare", "B. Gaborone", "C. Kampala", "D. Bamako"],
     "answer": "D"},
     
    {"Question": "What is the capital of Mauritius?",
     "Choices": ["A. Port Louis", "B. Victoria", "C. Monrovia", "D. Praia"],
     "answer": "A"},

    {"Question": "What is the capital of Equatorial Guinea?",
     "Choices": ["A. Nouakchott", "B. Malabo", "C. Moroni", "D. Conakry"],
     "answer": "B"} 
]

def run_quiz(questions):
    score = 0  # Initialize the score to zero

    # Loop through each question in the questions list
    for q in questions:
        print(q["Question"])  # Display the current question

        # Loop through each choice for the current question and print it
        for choice in q["Choices"]:
            print(choice)

        # Prompt the user for their answer and convert it to uppercase for consistency
        guess = input("Enter (A, B, C, D): ").upper()

        # Check if the user's guess matches the correct answer
        if guess == q["answer"]: 
            score += 1  # Increment the score if the answer is correct
            print("CORRECT!")  # Inform the user they got it right
        else:
            print(f"INCORRECT! The correct answer is {q['answer']}.")  # Inform the user of the correct answer

    # After all questions have been answered, display the results
    print("_______________")
    print("    RESULTS    ")
    print("_______________")
    print(f"Your final score is: {score}/{len(questions)}")  # Show final score out of total questions

# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    while True:  # Start an infinite loop to allow retaking the quiz
        run_quiz(questions)  # Call the run_quiz function to start the quiz
        
        # Ask if the user wants to retake the quiz
        retake = input("Would you like to retake the quiz? (yes/no): ").strip().lower()
        
        if retake != 'yes':  # If user does not want to retake, break out of the loop
            print("Thank you for your attempt! Goodbye!")  # Thank the user and exit
            break  # Exit the loop and end the program
