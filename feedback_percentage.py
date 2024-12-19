def calculate_positive_feedback_percentage(ratings):
    """Calculate the percentage of positive feedback (ratings 4 or 5)."""
    if not ratings:
        return "No ratings available."
    
    total_ratings = len(ratings)
    positive_ratings = sum(1 for rating in ratings if rating in [4, 5])
    percentage = (positive_ratings / total_ratings) * 100
    return f"Positive Feedback: {percentage:.2f}%"

def main():
    # Input ratings from the user
    try:
        ratings = list(map(int, input("Enter ratings (1-5) separated by spaces: ").split()))
        
        # Ensure all ratings are valid (between 1 and 5)
        if any(rating < 1 or rating > 5 for rating in ratings):
            print("Invalid ratings entered. Please enter numbers between 1 and 5 only.")
            return
        
        # Calculate and display positive feedback percentage
        result = calculate_positive_feedback_percentage(ratings)
        print(result)
    except ValueError:
        print("Invalid input. Please enter integers only.")

# Run the program
main()
