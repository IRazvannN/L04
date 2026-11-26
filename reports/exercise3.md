# Bug reports for exercise3.py

Line: 3
Problem: The function divides by len(numbers), which causes a ZeroDivisionError when the input list is empty, violating the docstring that states an empty list has average 0.
Example: average([]) raises ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: The function splits the text and returns the first word, but if the text is empty or only whitespace, split() returns an empty list, causing index out of range when accessing [0].
Example: first_word("") returns IndexError: list index out of range, expected "".
Fix: return text.split()[0] if text.strip() else ""

Line: 12
Problem: The function divides by total, which causes a ZeroDivisionError when total is 0, violating the docstring that states the result is 0 when total is 0.
Example: percent(5, 0) raises ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total else 0
