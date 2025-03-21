from calculator import summ, mull, fac, poww

def test_summ():
    assert summ(2, 3, 5) == 10
    assert summ(-111, 111) == 0
    assert summ(-1, -2, 3, 4) == 4
    

def test_mull():
    assert mull(2, 3, 5) == 30
    assert mull(1, 1, 1) == 1
    assert mull(189, 356, 0) == 0

def test_fac():
    assert fac(5) == 120
    assert fac(4) == 24
    assert fac(10) == 3628800

def test_poww():
    assert poww(2, 2) == 4
    assert poww(1, 100) == 1
    assert poww(5, 2) == 25