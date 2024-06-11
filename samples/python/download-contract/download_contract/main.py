import codecs
import requests
from email.message import Message
import os
import argparse
from dotenv import load_dotenv
import json


def get_env_var(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"{key} environment variable has not been set.")
    return value


if __name__ == "__main__":

    load_dotenv()

    parser = argparse.ArgumentParser(
        prog="ThoughtRiver",
        description="Download contract list and contract from ThoughtRiver",
    )

    parser.add_argument(
        "-f", "--format", default="DOCX", help="Download file as DOCX | HTML"
    )
    args = parser.parse_args()

    try:
        print("Loading environment variables:")
        thoughtriver_api_key = get_env_var("THOUGHTRIVER_API_KEY")
        print("THOUGHTRIVER_API_KEY: ********")
        thoughtriver_base_url = get_env_var("THOUGHTRIVER_BASE_URL")
        print(f"THOUGHTRIVER_BASE_URL: {thoughtriver_base_url}")
        print("")
    except Exception as ex:
        print(ex)
        exit(1)

    headers = {"X-API-Key": thoughtriver_api_key}
    list_contracts_url = f"{thoughtriver_base_url}/contract-management/latest/contracts"
    response = requests.get(
        list_contracts_url,
        headers=headers,
    )
    print("")

    if response.status_code == 200:
        contract_list = json.loads(response.content)
        number_contracts = len(contract_list["rows"])
        if number_contracts > 0:
            first_contract = contract_list["rows"][0]

            i = 0
            while i < number_contracts:
                contract = contract_list["rows"][i]
                print(
                    f"{contract['version_name']}, {contract['upload_date']}, {contract['version']['uuid']}, {contract['owner']['name']}"
                )
                i += 1

                if i == 5:
                    print(".\n.\n.\n")
                    i = number_contracts - 5

            download_format = args.format
            print(f"{download_format=}.")
            print("")

            download_url = f"{thoughtriver_base_url}/contract-content/latest/contract-versions/{first_contract['version']['uuid']}?format={download_format}"
            print(f"Downloadiing: {download_url=}")

            response = requests.get(download_url, headers=headers)

            if response.status_code == 200:
                msg = Message()
                msg["content-disposition"] = response.headers["content-disposition"]
                filename = msg.get_filename()

                with codecs.open(filename, "wb") as f:
                    f.write(response.content)

                print(f"Contract saved to file {filename=}")
            else:
                print(
                    f"Failed to download first contract from list [{response.status_code}]: {response.text}"
                )
        else:
            print(f"No contract available for download.")

    else:
        print(
            f"Failed to download list of contracts [{response.status_code}]: {response.text}"
        )
