"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.step_id
    import aws_sdk_deadline.types.task_id


class BatchGetTaskIdentifier(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the task.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the task.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID of the task.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID of the task.</p>"""
    task_id: "aws_sdk_deadline.types.task_id.TaskId"
    """<p>The task ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    out["taskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> BatchGetTaskIdentifier:
    out: BatchGetTaskIdentifier = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetTaskIdentifier.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetTaskIdentifier.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetTaskIdentifier.job_id required")
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("BatchGetTaskIdentifier.step_id required")
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("BatchGetTaskIdentifier.task_id required")
    return out
