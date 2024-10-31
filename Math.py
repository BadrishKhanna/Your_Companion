import random
import time

def math():
    def generate_basic_question():
        # Generate two random numbers for basic operations
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*', '/'])

        # Calculate the answer based on the operator
        if operator == '+':
            answer = num1 + num2
            question = f"What is {num1} + {num2}?"
        elif operator == '-':
            answer = num1 - num2
            question = f"What is {num1} - {num2}?"
        elif operator == '*':
            answer = num1 * num2
            question = f"What is {num1} * {num2}?"
        elif operator == '/':
            num1 = num1 * num2  # Adjust num1 to avoid division by zero
            answer = num1 // num2
            question = f"What is {num1} / {num2}?"

        return question, answer, 'basic'

    def generate_polynomial():
        # Generate a random polynomial of degree 2
        coeffs = [random.randint(1, 5) for _ in range(3)]  # Coefficients for x^2, x^1, and constant term
        polynomial = f"{coeffs[0]}*x**2 + {coeffs[1]}*x + {coeffs[2]}"
        return polynomial

    def differentiate(polynomial):
        # Simple differentiation based on polynomial rules
        terms = polynomial.split(" + ")
        derivatives = []

        for term in terms:
            if "*x**" in term:
                coeff, exp = term.split("*x**")
                new_coeff = int(coeff) * int(exp)
                new_exp = int(exp) - 1
                if new_exp > 1:
                    derivatives.append(f"{new_coeff}*x**{new_exp}")
                elif new_exp == 1:
                    derivatives.append(f"{new_coeff}*x")
                else:
                    derivatives.append(f"{new_coeff}")
            elif "*x" in term:
                coeff = term.split("*x")[0]
                derivatives.append(coeff)
            elif term.isdigit():
                continue  

        return " + ".join(derivatives) if derivatives else "0"

    def integrate(polynomial):
        terms = polynomial.split(" + ")
        integrals = []

        for term in terms:
            if "*x**" in term:
                coeff, exp = term.split("*x**")
                new_exp = int(exp) + 1
                integrals.append(f"{coeff}/{new_exp}*x**{new_exp}")  
            elif "*x" in term:
                coeff = term.split("*x")[0]
                integrals.append(f"{coeff}/2*x**2") 
            elif term.isdigit():
                integrals.append(f"{term}*x")  

        return " + ".join(integrals) + " + C"

    def format_fraction(expression):
        parts = expression.split(" + ")
        formatted_parts = []

        for part in parts:
            if '/' in part:
                numerator, denominator = part.split('/')
                formatted_parts.append(f"{numerator}/{denominator}")
            else:
                formatted_parts.append(part)

        return " + ".join(formatted_parts)

    def generate_calculus_question():
        polynomial = generate_polynomial()
        operation = random.choice(['differentiate', 'integrate'])

        if operation == 'differentiate':
            answer = differentiate(polynomial)
            question = f"What is the derivative of {polynomial}?"
        else:
            answer = integrate(polynomial)
            answer = format_fraction(answer) 
            question = f"What is the integral of {polynomial}?"

        return question, answer, operation

    def main():
        print("Welcome to the Dynamic Math Quiz!")

        num_questions = int(input("How many questions would you like to answer? "))
        score = 0

        for _ in range(num_questions):
            if random.choice([True, False]):  
                question, answer, question_type = generate_basic_question()
            else:
                question, answer, question_type = generate_calculus_question()

            start_time = time.time()  
            user_answer = input(question + " ")
            end_time = time.time()  

            time_taken = end_time - start_time  
            if question_type == 'basic':
                if user_answer.isdigit() and int(user_answer) == answer:
                    print(f"Correct! Time taken: {time_taken:.2f} seconds")
                    score += 1
                else:
                    print(f"Incorrect! The correct answer was {answer}. Time taken: {time_taken:.2f} seconds.")
            else:
            
                if user_answer.strip() == answer:
                    print(f"Correct! Time taken: {time_taken:.2f} seconds")
                    score += 1
                else:
                    print(f"Incorrect! The correct answer was {answer}. Time taken: {time_taken:.2f} seconds.")

        
        print(f"\nYou got {score} out of {num_questions} questions correct.")

    main()

if __name__ == "__main__":
    math()
