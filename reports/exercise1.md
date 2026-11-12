# Bug reports for exercise1.py

Line: 3
Problem: The condition checks if n % 2 == 1, which is true for odd numbers, not even numbers. For even numbers, n % 2 should equal 0.
Example: is_even(4) returns False, but it should return True
Fix: return n % 2 == 0

Line: 8
Problem: The function returns the sum of width and height, but the area of a rectangle is width multiplied by height.
Example: rectangle_area(3, 4) returns 7, but it should return 12
Fix: return width * height

Line: 13
Problem: The function adds 2 to n, but it should return twice the number, i.e., n multiplied by 2.
Example: double(5) returns 7, but it should return 10
Fix: return n * 2
