# Practicum 1 Tests - Problem 2
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

test_inputs = [
    (5,  1),
    (10, 4),
    (103, 100),
    (16384, 16383),
]
test_outputs = [
""" 5
-1
=4""",

""" 10
- 4
= 6""",

""" 103
-100
=  3""",

""" 16384
-16383
=    1"""
]

print(list(zip(test_inputs, test_outputs)))

@pytest.mark.parametrize("test_case", list(zip(test_inputs, test_outputs)))
def test_p2(test_case):
    args, expected = test_case
    output = run_with_args("p2", *args)
    assert output == expected


pytest.main(["p2_test.py",  "-vv", "--showlocals", "-p", "no:faulthandler"])

