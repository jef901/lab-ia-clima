import pytest
from app import calcular_impuesto

def test_calcular_impuesto_correcto():
    assert calcular_impuesto(100) == 22.0

def test_monto_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_impuesto(-50)
