"""Generated from Smithy shape ``com.amazonaws.iot#CreateJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.job_arn
    import aws_sdk_iot.types.job_description
    import aws_sdk_iot.types.job_id


class CreateJobResponse(TypedDict, closed=True):
    job_arn: NotRequired["aws_sdk_iot.types.job_arn.JobArn"]
    """<p>The job ARN.</p>"""
    job_id: NotRequired["aws_sdk_iot.types.job_id.JobId"]
    """<p>The unique identifier you assigned to this job.</p>"""
    description: NotRequired["aws_sdk_iot.types.job_description.JobDescription"]
    """<p>The job description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobResponse) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateJobResponse:
    out: CreateJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "description" in data:
        out["description"] = data["description"]
    return out
