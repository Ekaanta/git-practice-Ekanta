"""Main module"""
from datetime import date
from utils import add, subtract, multiply, divide

if __name__ == "__main__":
    print("Ekanta Banik Durjoy")
    print(f"Today's date: {date.today()}")
    
    # Test calculator functions
    print(f"\nCalculator Functions:")
    print(f"add(10, 5) = {add(10, 5)}")
    print(f"subtract(10, 5) = {subtract(10, 5)}")
    print(f"multiply(10, 5) = {multiply(10, 5)}")
    print(f"divide(10, 5) = {divide(10, 5)}")
    print(f"divide(20, 4) = {divide(20, 4)}")
    
    # Test error handling
    print(f"\nError Handling Tests:")
    print(f"divide(10, 0) = {divide(10, 0)}")
    print(f"add('10', 5) = {add('10', 5)}")
    print(f"multiply(7.5, 2) = {multiply(7.5, 2)}")
