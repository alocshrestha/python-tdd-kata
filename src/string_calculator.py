import re

class StringCalculator:
    def __init__(self):
        self.call_counter_for_add = 0

    def set_call_count_for_add(self, count: int):
        """
        Docstring for setCalledCount
        Sets the number of times the add function was called
        :param count: Description
        :return: Description
        :rtype: None
        """
        self.call_counter_for_add = count
    
    def calculate_string(self, calculate_me):
        """
        Calculates the sum of numbers in a comma-separated string.
        Allow only empty strings, single numbers, or two numbers.
        :param calculate_me: Description
        """
        if not calculate_me:
            return 0
        parts = calculate_me.split(',')
        if len(parts) == 1:
            return int(parts[0])
        elif len(parts) == 2:
            return sum(int(part) for part in parts)
        return -1


    def add(self, calculate_str) -> int:
        """
        Docstring for add
        Add any number of string contents if its a number or -ve number, 
        ignore other characters in the string
        
        :param calculate_str: Description
        :return: Description
        :rtype: int
        """
        self.call_counter_for_add += 1
        parts = re.split('[\n,;*%]+', calculate_str)
        negative_numbers = []
        sum_total = 0
        for part in parts:
            if part.startswith('-'):
                negative_numbers.append(part)
                continue
            sum_total += int(part) if part.lstrip('\n').isdigit() else 0
        if negative_numbers:
            raise ValueError(f"Negatives not allowed: {negative_numbers}")
        return sum_total


    def get_call_count_for_add(self) -> int:
        """
        Docstring for getCalledCount
        Returns the number of times the add function was called
        :return: Description
        :rtype: int
        """
        return self.call_counter_for_add