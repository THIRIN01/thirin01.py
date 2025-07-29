"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        pass
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = [n for n in numbers if n % 2 == 0]           
    odd_numbers = [n for n in numbers if n % 2 != 0]            
    
    # Calculate average
    average = sum(numbers) / len(numbers)                   
    
    # Numbers greater than average
    above_average = [n for n in numbers if n > average]        

    
    # Display results
    # Your code here

if __name__ == "__main__":
    number_operations()

def get_numbers():
    numbers = []
    print("Enter 10 numbers:")
    for i in range(10):
        while True:
            try:
                num = float(input(f"Number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return numbers

def number_operations():
    numbers = get_numbers()

    print(f"\nOriginal numbers: {numbers}")
    
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    
    total = sum(numbers)
    average = total / len(numbers)
    above_avg = [n for n in numbers if n > average]
    
    print("\n=== Filtered Lists ===")
    print(f"Even numbers        : {even}")
    print(f"Odd numbers         : {odd}")
    print(f"Above average ({average:.2f}): {above_avg}")

    print("\n=== Statistics ===")
    print(f"Sum    : {total}")
    print(f"Average: {average:.2f}")
    print(f"Min    : {min(numbers)}")
    print(f"Max    : {max(numbers)}")


    