"""Main module"""
from datetime import date
from utils import add, subtract, multiply

if __name__ == "__main__":
    print("Ekanta Banik Durjoy")
    print(f"Today's date: {date.today()}")
    
    # Test calculator functions
    print(f"\nCalculator Functions:")
    print(f"add(10, 5) = {add(10, 5)}")
    print(f"subtract(10, 5) = {subtract(10, 5)}")
    print(f"multiply(10, 5) = {multiply(10, 5)}")
