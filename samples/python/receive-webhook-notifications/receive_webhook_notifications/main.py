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

    Optionally the supplied URL can include the string {thoughtriver_version_id}
    anywhere within it, this will be searched and replaced with the contract
    version id by the ThoughtRiver Platform.

    This endpoint is specified by using the following f-string:

    f"{callback_base_url}/contract-processing-complete/{upload_unique_id}?tr_id={{thoughtriver_version_id}}"

    A successful 2xx reposne will indicate to the ThoughtRiver Platfrom that the
    callback has been received and there is no need to retry.

    The body of the response is not important but may be used for diagnostic
    puproses if required.
    """

    return {"supplied_unique_id": supplied_unique_id, "tr_id": tr_id}
