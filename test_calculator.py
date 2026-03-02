from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("✅ Add test passed!")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10
    print("✅ Subtract test passed!")

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    print("✅ Multiply test passed!")

def test_divide():
    assert divide(10, 2) == 5
    #assert divide(5, 0) == "Cannot divide by zero!"
    print("✅ Divide test passed!")

# Run all tests
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("🎉 All tests passed!")