"""Utility functions for calculator with error handling"""

def add(a, b):
    """Add two numbers with error handling"""
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Expected numbers, got {type(a).__name__} and {type(b).__name__}")
        return a + b
    except TypeError as e:
        return f"Error: {e}"

def subtract(a, b):
    """Subtract two numbers with error handling"""
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Expected numbers, got {type(a).__name__} and {type(b).__name__}")
        return a - b
    except TypeError as e:
        return f"Error: {e}"

def multiply(a, b):
    """Multiply two numbers with error handling"""
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Expected numbers, got {type(a).__name__} and {type(b).__name__}")
        return a * b
    except TypeError as e:
        return f"Error: {e}"

def divide(a, b):
    """Divide two numbers with error handling"""
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Expected numbers, got {type(a).__name__} and {type(b).__name__}")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    except (TypeError, ValueError) as e:
        return f"Error: {e}"
