import pandas as pd
import numpy as np
from pathlib import Path


class InputOutput:
    def __init__(self, input_path: Path, output_path: Path):
        self.input_path = input_path
        self.output_path = output_path
        self.check_file_exists()

    def check_file_exists(self):
        """Checks if the input file exists."""
        if not self.input_path.exists():
            raise FileNotFoundError(f"The input file {self.input_path} does not exist.")
        # we should also check that the output path directory
        # exists, but the file does not
        # to prevent overwriting existing files
        if not self.output_path.parent.exists():
            raise FileNotFoundError(
                f"The output directory {self.output_path.parent} does not exist."
            )
        if self.output_path.exists():
            raise FileExistsError(
                f"The output file {self.output_path} already exists. \
                Please choose a different name or delete the existing file."
            )

    def read_input_csv(self) -> pd.DataFrame:
        """Reads the input data from a CSV file."""
        return pd.read_csv(self.input_path, sep=r"\s+")

    def write_output_csv(self, data: pd.DataFrame) -> None:
        """Writes the output data to a CSV file."""
        data.to_csv(self.output_path, index=False)

    def read_input_numpy(self, skiprows: int = 1) -> np.ndarray:
        """Reads the input data from a NumPy file.

        Args:
            skiprows (int): Number of rows to skip at the beginning of the file.
        Returns:
            np.ndarray: The data read from the NumPy file.
        """
        return np.loadtxt(self.input_path, skiprows=skiprows)
