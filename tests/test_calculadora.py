import pytest
from src.calculadora import sumar, dividir

def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)