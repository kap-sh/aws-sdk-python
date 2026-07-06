"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.step_id


class BatchGetStepIdentifier(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the step.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the step.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID of the step.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    return out


def deserialize_json(data: dict) -> BatchGetStepIdentifier:
    out: BatchGetStepIdentifier = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetStepIdentifier.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetStepIdentifier.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetStepIdentifier.job_id required")
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("BatchGetStepIdentifier.step_id required")
    return out
