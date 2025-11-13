# built in
from pathlib import Path

# pip installed
from tqdm import tqdm

# our package
from calculator_pkg_jsk.calc import Calculator


class FileCalculator(Calculator):
    def sum_file(self, path=None) -> int:
        if path is None:
            path = Path(__file__).parent / "nums.csv"
        with tqdm(total=100_100_000, desc="Summing file") as pbar:
            total = 0
            with path.open() as f:
                for line in f:
                    total += int(line.strip())
                    pbar.update()
            return total
