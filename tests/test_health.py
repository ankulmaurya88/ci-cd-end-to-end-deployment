from app.health import is_system_healthy

def test_is_system_healthy():
    assert is_system_healthy() is True
