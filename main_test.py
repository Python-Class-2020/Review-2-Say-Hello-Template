import main

def test_main():
    assert main.say_hello(["Steve", "Mark", "Adam"]) == ["Hello Steve", "Hello Mark", "Hello Adam"]
    assert main.say_hello(["Micheal", "Jim", "Andy", "Stanley"]) == ["Hello Micheal", "Hello Jim", "Hello Andy", "Hello Stanley"]
