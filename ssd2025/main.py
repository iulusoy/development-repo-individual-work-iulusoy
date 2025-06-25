from input_output import InputOutput
from plot import PlotData
from pathlib import Path

if __name__ == "__main__":
    data_path = Path("data")
    input_file = "expec.t"
    input_path = data_path / input_file
    output_file = "output.csv"
    output_path = data_path / output_file
    io_obj = InputOutput(input_path, output_path)
    df = io_obj.read_input_csv()
    print(df.head())  # Display the first few rows of the DataFrame
    io_obj.write_output_csv(df)  # Write the DataFrame to a CSV file
    # plot the data
    output_file = "plot.png"
    plot_path = data_path / output_file
    plot_obj = PlotData(filename=plot_path, type="line")
    plot_obj.plot(
        x=df["time"].to_numpy(),
        y=df["<z>"].to_numpy(),
    )
