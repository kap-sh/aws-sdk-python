"""Generated from Smithy shape ``com.amazonaws.deadline#JobAttachmentDetailsIdentifiers``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_id


class JobAttachmentDetailsIdentifiers(TypedDict):
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobAttachmentDetailsIdentifiers) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> JobAttachmentDetailsIdentifiers:
    out: JobAttachmentDetailsIdentifiers = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobAttachmentDetailsIdentifiers.job_id required")
    return out
