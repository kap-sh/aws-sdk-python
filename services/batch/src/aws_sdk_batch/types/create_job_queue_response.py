"""Generated from Smithy shape ``com.amazonaws.batch#CreateJobQueueResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class CreateJobQueueResponse(TypedDict):
    job_queue_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the job queue.</p>"""
    job_queue_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobQueueResponse) -> dict:
    out: dict = {}
    if "job_queue_name" in value:
        out["jobQueueName"] = value["job_queue_name"]
    if "job_queue_arn" in value:
        out["jobQueueArn"] = value["job_queue_arn"]
    return out


def deserialize_json(data: dict) -> CreateJobQueueResponse:
    out: CreateJobQueueResponse = {}  # type: ignore[typeddict-item]
    if "jobQueueName" in data:
        out["job_queue_name"] = data["jobQueueName"]
    if "jobQueueArn" in data:
        out["job_queue_arn"] = data["jobQueueArn"]
    return out
