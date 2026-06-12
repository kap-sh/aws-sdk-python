"""Generated from Smithy shape ``com.amazonaws.mgn#DeleteJobRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_mgn.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.job_id

class DeleteJobRequest(TypedDict):
    job_id: "aws_sdk_mgn.types.job_id.JobID"
    """<p>Request to delete Job from service by Job ID.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Request to delete Job from service by Account ID.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobRequest) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> DeleteJobRequest:
    out: DeleteJobRequest = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    else:
        raise DeserializationError("DeleteJobRequest.job_id required")
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out