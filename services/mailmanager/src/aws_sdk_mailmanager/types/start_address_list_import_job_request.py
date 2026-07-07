"""Generated from Smithy shape ``com.amazonaws.mailmanager#StartAddressListImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.job_id


class StartAddressListImportJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_mailmanager.types.job_id.JobId"
    """<p>The identifier of the import job that needs to be started.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartAddressListImportJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartAddressListImportJobRequest:
    out: StartAddressListImportJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StartAddressListImportJobRequest.job_id required")
    return out
