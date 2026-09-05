# Remove in M2
from credit_engine import calc


def test_add_two_numbers():
    resultado = calc.add(2, 5) # ACT
    assert resultado == 7 # ASSERT

