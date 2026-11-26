import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_hardcoded_password():
    assert ADMIN_PASSWORD != "admin123"
    assert not check_admin("admin123")


# bug report 2
def test_r2_sql_injection():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, email TEXT)")
    db.execute("INSERT INTO users VALUES ('ana', 'ana@mail.com')")
    assert find_user(db, "'; DROP TABLE users; --") is None
