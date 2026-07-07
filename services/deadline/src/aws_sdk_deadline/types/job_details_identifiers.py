"""Generated from Smithy shape ``com.amazonaws.deadline#JobDetailsIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_id


class JobDetailsIdentifiers(TypedDict, closed=True):
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetailsIdentifiers) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> JobDetailsIdentifiers:
    out: JobDetailsIdentifiers = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobDetailsIdentifiers.job_id required")
    return out
