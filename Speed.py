import random
import time

def speed():
    def typing_test():
        text_to_type = [
            'The one who is destined to lose never accepts it.',
            'The quick brown fox jumps over the lazy dog.',
            'The lion is the king of the jungle.',
            'I am the person who is typing.'
        ]

        print("Press Enter to start the typing test...")
        input()  

        
        sentence_to_type = random.choice(text_to_type)

        print("Type the following sentence as fast as you can:")
        print(sentence_to_type)

        
        start_time = time.time()

        
        user_input = input("Your typing: ")
        end_time = time.time()
        time_taken = end_time - start_time
        time_taken_minutes = time_taken / 60  
        if user_input == sentence_to_type:
            print(f"Correct! Time taken: {time_taken:.2f} seconds")
            accuracy = 100  
        else:
            print(f"Incorrect! The correct sentence was: '{sentence_to_type}'")
            print(f"Time taken: {time_taken:.2f} seconds")

            
            correct_chars = sum(1 for a, b in zip(user_input, sentence_to_type) if a == b)
            accuracy = (correct_chars / len(sentence_to_type)) * 100 if sentence_to_type else 0

        
        total_words_typed = len(user_input.split())
        wpm = total_words_typed / time_taken_minutes if time_taken_minutes > 0 else 0

        
        print(f"Your accuracy: {accuracy:.2f}%")
        print(f"Words per minute: {wpm:.2f} WPM")

    typing_test()

if __name__ == "__main__":
    speed()
