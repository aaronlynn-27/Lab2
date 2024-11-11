
import lab2 as temp


def test_min_max():
    temperatures = [34.9, 13.0, 32.4, 28.1, 29.5, 27.9]
    result = temp.find_min_max(temperatures)
    assert (result == [13.0, 34.9])
    
def test_calc_average():
    temperatures = [34.9, 13.0, 32.4, 28.1, 29.5, 27.9]
    result = temp.calc_average(temperatures)
    expected = (34.9 + 13.0 + 32.4 + 28.1 + 29.5 + 27.9)/6
    assert abs(result - expected) < 1e-6


def test_calc_median_temperature():
    temperatures = [34.9, 13.0, 32.4, 28.1, 29.5, 27.9]
    sorted_temp = temp.sort_temp(temperatures)
    result = temp.cal_median(sorted_temp)
    expected = (28.1 + 29.5)/2
    assert result == expected

    temperatures = [34.9, 13.0, 32.4, 29.5, 27.9]
    sorted_temp = temp.sort_temp(temperatures)
    result = temp.cal_median(sorted_temp)
    expected = 29.5
    assert abs(result - expected) < 1e-6
