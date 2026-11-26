# Bug reports for exercise4.py

Line: 4
Problem: Hardcoded secret exposes credentials in source code instead of reading from environment variables.
Example: check_admin("admin123") returns True, expected False when ADMIN_PASSWORD is unset.
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

Line: 14
Problem: SQL injection vulnerability via string concatenation in f-string; allows malicious input to alter query logic.
Example: find_user(db, "'; DROP TABLE users; --") executes malicious SQL and could delete user data.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
