### Test Internals

import subprocess

# python3 -m homework data/input data/output
from ...wordcount import parse_args


def test_parse_args():

    result = subprocess.run(
        ["python", "-m", "homework", "data/input/", "data/output/"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "input: data/input/" in result.stdout
    assert "output: data/output/" in result.stdout