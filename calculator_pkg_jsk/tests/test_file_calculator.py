from calculator_pkg_jsk.file_calculator import FileCalculator


def test_file_calculator():
    assert FileCalculator().sum_file() == 6
