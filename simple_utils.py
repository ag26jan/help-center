# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverses the characters in a string.
    
    Returns:
        reversed_text (str): The input string with characters in reverse order.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count whitespace-separated words in a string.
    
    Parameters:
        sentence (str): Input text whose words are separated by whitespace.
    
    Returns:
        int: Number of words in `sentence`.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
    	celsius (float|int): Temperature in degrees Celsius.
    
    Returns:
    	fahrenheit (float): Equivalent temperature in degrees Fahrenheit computed as (celsius * 9/5) + 32.
    """
    return (celsius * 9/5) + 32