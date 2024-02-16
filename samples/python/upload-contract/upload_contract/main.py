import string
import random
import requests
import mimetypes
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
        prog="ThoughtRiver", description="Upload a contract to ThoughtRiver"
    )

    parser.add_argument("document")
    parser.add_argument("-dt", "--deal-type")

    args = parser.parse_args()

    try:
        print("Loading environment variables:")
        thoughtriver_api_key = get_env_var("THOUGHTRIVER_API_KEY")
        print("THOUGHTRIVER_API_KEY: ********")
        thoughtriver_base_url = get_env_var("THOUGHTRIVER_BASE_URL")
        print(f"THOUGHTRIVER_BASE_URL: {thoughtriver_base_url}")
        callback_base_url = get_env_var("CALLBACK_BASE_URL")
        print(f"CALLBACK_BASE_URL: {callback_base_url}")
        print("")
    except Exception as ex:
        print(ex)
        exit(1)

    upload_unique_id = "".join(random.choice(string.ascii_lowercase) for i in range(10))
    print(
        f"Created upload unique id to track uploads to ThoughtRiver IDs: {upload_unique_id}"
    )
    print("")

    webhook_url = f"{callback_base_url}/contract-processing-complete/{upload_unique_id}?tr_id={{thoughtriver_version_id}}"
    print("Request a callback from ThoughtRiver Platform to a unique url.")
    print(
        "Optionally include the ThoughtRiver version is to be included in the response"
    )
    print(webhook_url)
    print("")

    headers = {"X-API-Key": thoughtriver_api_key}
    with open(args.document, "rb") as f:
        content_type, _ = mimetypes.guess_type(f.name)
        upload_url = f"{thoughtriver_base_url}/contract-management/latest/contracts"
        params = {"callback_url": webhook_url, "deal_type_code": args.deal_type}
        files = {"document": (f.name, f, content_type)}

        print(f"upload to: {upload_url}")
        response = requests.post(
            upload_url, headers=headers, params=params, files=files
        )
        print("")

    uploaded_contract_ids = json.loads(response.content)

    if response.status_code == 201:
        print(
            f"These IDs should be stored by the uploading system against the upload unique id [{upload_unique_id}] created above."
        )
        print("They are used to retrieve information about the processed contract.")
        print(f"Contract ID:\t{uploaded_contract_ids['contract_uuid']}")
        print(f"Version ID:\t{uploaded_contract_ids['version_uuid']}")
        print("")

        print(
            "Please await your callback via the web hook provided, or monitor the contract via the ThoughtRiver App."
        )
        print("")

        input("Once the callback is recieved, press Enter to load report...")
        report_url = f"{thoughtriver_base_url}/contract-content/latest/contract-versions/{uploaded_contract_ids['version_uuid']}/report"
        print(report_url)

        response = requests.get(report_url, headers=headers)

        if response.status_code == 200:
            contract_report = json.loads(response.content)

            if len(contract_report["rows"]) > 0:
                print(
                    "%-54s%-62s%-18s%-8s%s"
                    % ("dfcode", "name", "value", "clauses", "issue_summary")
                )
                for row in contract_report["rows"]:
                    print(
                        "%-54s%-62s%-18s%-8i%s"
                        % (
                            row["property_dfcode"],
                            row["property_name"],
                            row["property_value"],
                            len(row["property_linked_clauses"]),
                            row["issue_summary"] if row["issue_summary"] else "-",
                        )
                    )
            else:
                print(
                    "No properties returned for this contract version.  Did you receive the callback via the web hook provided?"
                )
        else:
            print(
                "Failed to load contract version data [{response.status_code}]: {response.text}"
            )
    else:
        print(f"Failed to upload contract [{response.status_code}]: {response.text}")
