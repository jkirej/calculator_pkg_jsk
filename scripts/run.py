from calculator_pkg_jsk import Calculator
from calculator_pkg_jsk.file_calculator import FileCalculator
from pathlib import Path

print(Calculator().add(1,2))
FileCalculator().sum_file(Path("~/Desktop/nums.csv").expanduser())

