from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/contract-processing-complete/{supplied_unique_id}")
def contract_processing_complete(supplied_unique_id: str, tr_id: str = None):
    """
    WebHook Callback to be supplied to the ThoughtRiver Platfrom on contract upload
    via the .../contract-management/latest/contracts end point.

    The URL can be any pattern required, it is reccomended that the calling code
    inlude a supplier unique id within the URL.

    Optionally the supplied URL can include the following string url parameters
    anywhere within it - these will be searched and replaced by the ThoughtRiver platform.
        {thoughtriver_version_id} - The ThoughtRiver contract_version_id of the uploaded contract.
        {status} - The status of the upload as determined by the ThoughtRiver Platform.
    Current statuses are:
        - success
        - awaiting_party_confirmation
        - fail_converting_files
        - fail_reading_word_document
        - fail_storing_paragraphs
        - fail_detecting_parties
        - fail_preprocessing_paragraphs
        - fail_asking_lexible_questions
        - fail_extracting_values
        - fail_detecting_familiarity
        - fail_updating_issues
    Where `success` indicates that the contract has been successfully processed, `awating_*` indicates
    a user action is needed, and `fail_*` indicates that the contract has failed during the processing
    and identifies at which step that failure has occurred.

    This endpoint is specified by using the following f-string:

    f"{callback_base_url}/contract-processing-complete/{upload_unique_id}?tr_id={{thoughtriver_version_id}}&upload_status={{status}}"

    A successful 2xx reposne will indicate to the ThoughtRiver Platfrom that the
    callback has been received and there is no need to retry.

    The body of the response is not important but may be used for diagnostic
    puproses if required.
    """

    return {"supplied_unique_id": supplied_unique_id, "tr_id": tr_id}
