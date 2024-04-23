# MacroTrend data scrapper

Motivation: This package is designed to learn and
implement web scrapping.

Pros: Clever csv file update. 
Imagine you would like to scrap some parameters, and apply
some operations to them to obtain some result. You determined
your scrap parameters, those were scrapped and saved. Then, you
realized that you forgot to add some parameters to your scrap
parameters. In this case, it is not necessary to rescrap everything
including the parameters you forgot. Simply, scrap what you forgot
it will be automatically added as an extra column to existing csv file.

Limitations: This scrapper is designed to perform scrapping only
on stock screen table.

Package for scrapping the desired data from the [MacroTrend stocks screner](https://www.macrotrends.net/stocks/stock-screener) and saving it into a `.csv` file.

![alt text](readme_images/tableExplainer.png)

An example of the scrapped data in a `.csv` file is given below.

![alt text](readme_images/excel.PNG)

First column and the second column of the `.csv` are always
set to `Ticker` and `name`, respectively.

## Installation

### Prerequisites

- Python 3.x is installed to your system

### Installation steps

1. Clone this repository to your local machine

   ```bash
   git clone git@github.com:AlpSari/MagicInvest.git
   ```

2. Go to the directory

   ```bash
   cd MagicInvest
   ```

3. (Optional) Create a Python virtual environment and activate it:

   ```bash
   python -m venv .venv/
   ```

   From Windows command prompt (i.e., cmd), activate the virtual environment by:

   ```bash
   .venv/Scripts/activate
   ```

4. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Running the data scrapper

To run the data scrapper:

```bash
python main.py [arguments]
```

Running `main.py` without any arguments will open the GUI below for user to
select which parameters are to be scrapped and the scrapped data will be stored
in `Output.csv` in the current working directory. Run `python main.py -h` for
the list of the available arguments. The arguments are also explained below.

![alt text](readme_images/parameterGUI.PNG)

#### Arguments of main.py

- ` --parameters-path `: Path to the `JSON` file which stores the parameters to
be scrapped. User can avoid using the GUI by creating a `JSON` file (storing
parameters to be scrapped) and providing its path via this argument.

   Format of the `JSON` file:

   ```json
   ["param1", "param2", "...", "paramN"]
   ```

- ` --output-csv `: Name of the `CSV` file to which scrapped parameters are
  saved. Default is `Output.csv`.

- ` --logging-level `: Controls the logging level. The valid arguments are
  `["none", "info", "debug"]`. Default is set to `none`.

Example usage with the arguments:

```bash
python main.py --parameters-path this/is/my/path.JSON --output-csv my_file.csv --logging-level none
```

## Note To Developers

Developers should use the same code checking tools with the same settings that
are configured in the root directory. All the tools and plugins for development
can be downloaded using:

```bash
pip install -r dev_requirements.txt
```

## Testing

Unit tests for the package are available in the `tests/` directory. To run the tests, use the following command:

```bash
python -m unittest discover -v tests
```

Note that some of the GUI-related tests are causing display errors (in the remote server); therefore, those are not implemented yet.
