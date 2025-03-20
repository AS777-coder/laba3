from calculator import summ, mull, fac, poww

def test_summ():
    assert summ(2, 3, 5) == 10

def test_mull():
    assert mull(2, 3, 5) == 30

def test_fac():
    assert fac(5) == 120

def test_poww():
    assert poww(2, 2) == 4