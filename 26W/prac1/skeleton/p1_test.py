# Practicum 1 Tests - Problem 1
import pytest
import subprocess

def run_with_args(filename, *args):
    args = [str(a) for a in args]
    try:
        command = ["python3", filename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")
    except:
        command = ["python", filename + ".py", *args]
        return subprocess.check_output(command, text=True).rstrip("\n")

test_cases = [
    ((1, 2, 3, 4), ("1 / 2 is 0.5", "3 / 4 is 0.75", "Their difference is 0.25")),
    ((1, 2, 5, 8), ("1 / 2 is 0.5", "5 / 8 is 0.625", "Their difference is 0.125")),
    ((6, 8, 2, 5), ("6 / 8 is 0.75", "2 / 5 is 0.4", "Their difference is -0.35")),
    ((8, 5, 7, 2), ("8 / 5 is 1.6", "7 / 2 is 3.5", "Their difference is 1.9")),
]

@pytest.mark.parametrize("test_case", test_cases)
def test_line1(test_case):
    args, expected = test_case
    output = run_with_args("p1", *args)
    assert output.split('\n')[0] == expected[0]

@pytest.mark.parametrize("test_case", test_cases)
def test_line2(test_case):
    args, expected = test_case
    output = run_with_args("p1", *args)
    assert output.split('\n')[1] == expected[1]
    
@pytest.mark.parametrize("test_case", test_cases)
def test_line3(test_case):
    args, expected = test_case
    output = run_with_args("p1", *args)
    assert output.split('\n')[2] == expected[2]


pytest.main(["p1_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])
