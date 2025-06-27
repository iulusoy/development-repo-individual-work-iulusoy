import input_output as io
import pytest
from pathlib import Path


@pytest.fixture
def input_output_instance(tmp_path):
    """Fixture to create an InputOutput instance with temporary paths."""
    input_path = tmp_path / "input.csv"
    output_path = tmp_path / "output.csv"
    input_path.write_text("col1\tcol2\n1\t2\n3\t4")
    return io.InputOutput(input_path=Path(input_path), output_path=Path(output_path))


def test_read_input_csv(input_output_instance):
    """Test reading input CSV file."""
    df = input_output_instance.read_input_csv()
    assert not df.empty
    assert list(df.columns) == ["col1", "col2"]
    assert df.shape == (2, 2)
    assert df.iloc[0, 0] == 1
    assert df.iloc[0, 1] == 2
