import numpy
import pytest
import year2024.utility as utility
from pandas import DataFrame
from pathlib import Path


@pytest.mark.parametrize(
    "file_path, expected",
    [
        (
            r"year2024\day01\solution.py",
            Path(rf"year2024\day01\resource\{utility.INPUT_FILE_NAME}"),
        ),
        (
            r"year2024\day01\test\test_solution.py",
            Path(rf"year2024\day01\test\resource\{utility.INPUT_FILE_NAME}"),
        ),
    ],
)
def test_get_input_file_path(file_path: str, expected: Path) -> None:
    assert utility.get_input_file_path(file_path) == expected


@pytest.mark.parametrize(
    "file_path, expected",
    [
        (
            Path(r"year2024\test\resource\test_get_column_labels_fixed.csv"),
            [0, 1, 2],
        ),
        (
            Path(r"year2024\test\resource\test_get_column_labels_variable.csv"),
            [0, 1, 2],
        ),
    ],
)
def test_get_column_labels(file_path: Path, expected: list[int]) -> None:
    assert utility.get_column_labels(file_path) == expected


def test_get_input() -> None:
    file_path: Path = Path(rf"year2024\test\resource\test_get_input.csv")

    expected: DataFrame = DataFrame(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
    )

    assert utility.get_input(file_path).equals(expected)


@pytest.mark.parametrize(
    "day, parts, expected",
    [
        (
            1,
            {"part_1": 1},
            "day 1: part 1: answer: 1",
        ),
        (
            1,
            {"part_1": 1, "part_2": 2},
            ("day 1: part 1: answer: 1\n" "day 1: part 2: answer: 2"),
        ),
    ],
)
def test_get_answer_message(day: str, parts: dict[str, int], expected: str) -> None:
    assert utility.get_answer_message(day, **parts) == expected
