"""Generated from Smithy shape ``com.amazonaws.batch#SubmitJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class SubmitJobResponse(TypedDict):
    job_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the job.</p>"""
    job_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the job.</p>"""
    job_id: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The unique identifier for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmitJobResponse) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> SubmitJobResponse:
    out: SubmitJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    return out
