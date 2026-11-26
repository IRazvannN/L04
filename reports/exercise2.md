# Bug reports for exercise2.py

Line: 2
Problem: is_passing uses > instead of >=, so grades of exactly 5 return False instead of True.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password uses > 8 instead of >= 8, rejecting valid 8-character inputs containing digits.
Example: is_valid_password("pass1234") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: clamp uses min(x, low) inside max(low, min(x, low)), which incorrectly clamps below low; it should clamp between low and high.
Example: clamp(3, 1, 10) returns 1, expected 3 (since 3 is above low but below high, it should return 3, not 1).
Fix: return max(low, min(x, high))
