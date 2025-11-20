def display_movies(movies):
    """Display all available movies with their details"""
    print("\n" + "="*60)
    print("AVAILABLE MOVIES".center(60))
    print("="*60)
    
    for movie_id, details in movies.items():
        print(f"\n{movie_id}. {details['title']}")
        print(f"   Showtimes: {', '.join(details['showtimes'])}")
        print(f"   Price per ticket: ${details['price']:.2f}")
    print("="*60)


def get_movie_choice(movies):
    """Get and validate movie selection from user"""
    while True:
        try:
            choice = int(input("\nEnter movie number (1-5): "))
            if choice in movies:
                return choice
            else:
                print("Invalid movie number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def get_showtime_choice(showtimes):
    """Get and validate showtime selection"""
    print("\nAvailable showtimes:")
    for i, time in enumerate(showtimes, 1):
        print(f"{i}. {time}")
    
    while True:
        try:
            choice = int(input(f"\nSelect showtime (1-{len(showtimes)}): "))
            if 1 <= choice <= len(showtimes):
                return showtimes[choice - 1]
            else:
                print("Invalid showtime number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def get_ticket_quantity():
    """Get and validate number of tickets"""
    while True:
        try:
            quantity = int(input("\nHow many tickets? (1-10): "))
            if 1 <= quantity <= 10:
                return quantity
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")


def confirm_booking(movie_title, showtime, quantity, total_price):
    """Display booking details and confirm"""
    print("\n" + "-"*60)
    print("BOOKING SUMMARY".center(60))
    print("-"*60)
    print(f"Movie: {movie_title}")
    print(f"Showtime: {showtime}")
    print(f"Number of tickets: {quantity}")
    print(f"Total price: ${total_price:.2f}")
    print("-"*60)
    
    while True:
        confirm = input("\nConfirm this booking? (yes/no): ").lower().strip()
        if confirm in ['yes', 'y', 'no', 'n']:
            return confirm in ['yes', 'y']
        else:
            print("Please enter 'yes' or 'no'.")


def want_another_booking():
    """Ask if user wants to book another movie"""
    while True:
        response = input("\nWould you like to book another movie? (yes/no): ").lower().strip()
        if response in ['yes', 'y', 'no', 'n']:
            return response in ['yes', 'y']
        else:
            print("Please enter 'yes' or 'no'.")


def display_final_summary(bookings, total_cost):
    """Display final booking summary"""
    print("\n" + "="*60)
    print("FINAL BOOKING SUMMARY".center(60))
    print("="*60)
    
    if not bookings:
        print("\nNo bookings made.")
    else:
        print(f"\nTotal bookings: {len(bookings)}")
        print("\nBooking details:")
        for i, booking in enumerate(bookings, 1):
            print(f"\n{i}. {booking['movie']}")
            print(f"   Showtime: {booking['showtime']}")
            print(f"   Tickets: {booking['quantity']}")
            print(f"   Cost: ${booking['cost']:.2f}")
        
        print("\n" + "-"*60)
        print(f"TOTAL COST: ${total_cost:.2f}")
        print("="*60)


def main():
    # Movie database with nested dictionaries
    movies = {
        1: {
            "title": "The Quantum Paradox",
            "showtimes": ["10:00 AM", "1:30 PM", "5:00 PM", "8:30 PM"],
            "price": 12.50
        },
        2: {
            "title": "Love in Paris",
            "showtimes": ["11:00 AM", "2:00 PM", "6:30 PM", "9:00 PM"],
            "price": 10.00
        },
        3: {
            "title": "Galaxy Warriors: Return",
            "showtimes": ["10:30 AM", "2:30 PM", "6:00 PM", "9:30 PM"],
            "price": 15.00
        },
        4: {
            "title": "The Mystery House",
            "showtimes": ["12:00 PM", "3:30 PM", "7:00 PM", "10:00 PM"],
            "price": 11.50
        },
        5: {
            "title": "Comedy Night Live",
            "showtimes": ["1:00 PM", "4:00 PM", "7:30 PM", "10:30 PM"],
            "price": 9.50
        }
    }
    
    bookings = []
    total_cost = 0
    
    print("\n" + "="*60)
    print("WELCOME TO CINEMAPLEX BOOKING SYSTEM".center(60))
    print("="*60)
    
    while True:
        # Display available movies
        display_movies(movies)
        
        # Get movie choice
        movie_choice = get_movie_choice(movies)
        selected_movie = movies[movie_choice]
        
        # Get showtime
        selected_showtime = get_showtime_choice(selected_movie["showtimes"])
        
        # Get number of tickets
        ticket_quantity = get_ticket_quantity()
        
        # Calculate total price
        booking_cost = selected_movie["price"] * ticket_quantity
        
        # Confirm booking
        if confirm_booking(
            selected_movie["title"],
            selected_showtime,
            ticket_quantity,
            booking_cost
        ):
            # Add to bookings
            bookings.append({
                "movie": selected_movie["title"],
                "showtime": selected_showtime,
                "quantity": ticket_quantity,
                "cost": booking_cost
            })
            total_cost += booking_cost
            print("\n✓ Booking confirmed!")
        else:
            print("\n✗ Booking cancelled.")
        
        # Ask if they want to book another movie
        if not want_another_booking():
            break
    
    # Display final summary
    display_final_summary(bookings, total_cost)
    print("\nThank you for using Cinemaplex! Enjoy your movies! 🎬")


if __name__ == "__main__":
    main()
