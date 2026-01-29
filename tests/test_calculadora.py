import pytest
from src.calculadora import sumar, dividir, restar

def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_restar_positivos():
    assert restar(5, 3) == 2