"""Generated from Smithy shape ``com.amazonaws.location#GetJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.job_id


class GetJobRequest(TypedDict):
    job_id: "aws_sdk_location.types.job_id.JobId"
    """<p>The unique identifier of the job to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJobRequest:
    out: GetJobRequest = {}  # type: ignore[typeddict-item]
    return out
