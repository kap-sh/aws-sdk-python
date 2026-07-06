"""Generated from Smithy shape ``com.amazonaws.location#CancelJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.job_id


class CancelJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_location.types.job_id.JobId"
    """<p>The unique identifier of the job to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CancelJobRequest:
    out: CancelJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("CancelJobRequest.job_id required")
    return out
