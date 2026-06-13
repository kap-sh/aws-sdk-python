"""Generated from Smithy shape ``com.amazonaws.drs#DeleteJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.job_id


class DeleteJobRequest(TypedDict):
    job_id: "aws_sdk_drs.types.job_id.JobID"
    """<p>The ID of the Job to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobRequest) -> dict:
    out: dict = {}
    out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> DeleteJobRequest:
    out: DeleteJobRequest = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    else:
        raise DeserializationError("DeleteJobRequest.job_id required")
    return out
