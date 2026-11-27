"""Authentication fixtures for API tests."""
TEST_PASSWORD = "123demo"


def seed_demo():
    import seed
    seed.seed()


def sign_in(client, test_api="", username="demo123"):
    response = client.post(f"{test_api}/auth/login", json={"username": username, "password": TEST_PASSWORD})
    response.raise_for_status()
    return response
