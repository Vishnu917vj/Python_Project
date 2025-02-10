from src.Math import add,sub
def test_add():
    assert add(1,2)==3
    assert add(2,3)==5
def test_sub():
    assert sub(3,2)==1
    assert sub(8,7)==1