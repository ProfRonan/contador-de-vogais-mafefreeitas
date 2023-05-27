"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    """
    Takes in a string and returns the number of vowels in the string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
"""This program counts the number of vowels in a string."""
    vogais = "aeiou"  
    resultado = 0 

    for caractere in string.lower():
        if caractere in vogais:
            resultado += 1

    return resultado

palavra = input("Digite uma palavra qualquer: ")
numero_vogais = count_vowels(palavra)
print("O numero de vogais é:", numero_vogais)
