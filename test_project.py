import pytest
from project import inflation_rate, real_balances, is_hyperinflation, load_data, adaptive_expectations

def test_inflation_rate():
    assert inflation_rate(100, 150) == 50
    assert inflation_rate(150, 300) == 100
    assert inflation_rate(200, 100) == -50
    with pytest.raises(ValueError):
        inflation_rate(0, 100)

def test_real_balances():
    assert real_balances(500, 100) == 5
    assert real_balances(1200, 300) == 4
    assert round(real_balances(700, 150), 2) == 4.67
    with pytest.raises(ValueError):
        real_balances(100, 0)

def test_is_hyperinflation():
    assert is_hyperinflation(60) == True
    assert is_hyperinflation(40) == False
    assert is_hyperinflation(50) == False
    assert is_hyperinflation(13000, yearly=True) == True
    assert is_hyperinflation(100, yearly=True) == False

def test_load_data():
    data = load_data("data.csv")
    assert len(data) == 30
    assert data[0]["year"] == 1990
    assert data[0]["price_index"] == 33.39
    assert data[22]["money_supply"] == None

def test_adaptive_expectations():
    assert adaptive_expectations([10, 20, 20], 0.5) == [10, 15, 17.5]
    assert adaptive_expectations([10, 20, 30], 1) == [10, 20, 30]
    assert adaptive_expectations([10, 20, 30], 0) == [10, 10, 10]
    with pytest.raises(ValueError):
        adaptive_expectations([10, 20, 30], 2)
        

