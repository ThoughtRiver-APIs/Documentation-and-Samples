## Download a Contract List and Contract from ThoughtRiver

This sample downloads the full list of contracts the API Key has access to and downloads the latest contract from the ThoughtRiver Platform.

The sample will output the first and last 5 contracts the user can view to the console prior to downloading.

The contract can be downloaded as `DOCX` or `HTML`. The format can be set with the `-f`, `--format` command line option. 

## Installing and running the sample

From a terminal, located within the `download-contract` folder:

### Installation

- Create a new virtual environment 
  - `python -m venv .venv`
- Activate the virtual environment 
  - If on a Mac or Unix based environment run: `source .venv/bin/activate`
  - If on a Windows based environment run: `.venv/Scripts/activate`
  - Please note that if you are running on a Windows based environment you may experience the error '.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system'.
    This can be resolved by [enabling scripts](https:/go.microsoft.com/fwlink/?LinkID=135170).
- Install the following requirements
  - `pip install requests`
  - `pip install python-dotenv`
- create a .env file within the `download-contract/download_contract` folder and specify the following environment variables:
  - `THOUGHTRIVER_API_KEY={your_key}`
  - `THOUGHTRIVER_BASE_URL=https://api2-{your_region}.thoughtriver.review/api`

### Running the sample

From a terminal, located within the `download-contract/download_contract` folder:

run:  `python -m main -f DOCX` or `python -m main -f HTML`