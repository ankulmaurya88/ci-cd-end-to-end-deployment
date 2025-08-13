from app.string_ops import reverse_string, is_palindrome

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_is_palindrome():
    assert is_palindrome("level") is True
    assert is_palindrome("test") is False
