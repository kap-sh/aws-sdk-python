"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetAddressListImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.job_id


class GetAddressListImportJobRequest(TypedDict):
    job_id: "aws_sdk_mailmanager.types.job_id.JobId"
    """<p>The identifier of the import job that needs to be retrieved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAddressListImportJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAddressListImportJobRequest:
    out: GetAddressListImportJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("GetAddressListImportJobRequest.job_id required")
    return out
