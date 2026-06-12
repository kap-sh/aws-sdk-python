"""Generated from Smithy shape ``com.amazonaws.batch#DescribeServiceJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class DescribeServiceJobRequest(TypedDict):
    job_id: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The job ID for the service job to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeServiceJobRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> DescribeServiceJobRequest:
    out: DescribeServiceJobRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    return out
