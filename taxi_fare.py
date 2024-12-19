def calculate_fare(distance):
    """Calculate the fare for a single trip."""
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare

def main():
    try:
        # Input the trips as a list of distances
        trips = list(map(int, input("Enter distances for trips (in km) separated by spaces: ").split()))
        
        if not trips:
            print("No trips entered.")
            return
        
        total_fare = 0

        # Calculate fare for each trip
        for i, distance in enumerate(trips, start=1):
            fare = calculate_fare(distance)
            print(f"Trip {i}: ${fare}")
            total_fare += fare

        # Display total fare
        print(f"Total Fare: ${total_fare}")
    except ValueError:
        print("Invalid input. Please enter distances as integers.")
main()
