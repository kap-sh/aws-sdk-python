"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_update_task_error_code
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.step_id
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.task_id


class BatchUpdateTaskError(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the task that could not be updated.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the task that could not be updated.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID of the task that could not be updated.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID of the task that could not be updated.</p>"""
    task_id: "aws_sdk_deadline.types.task_id.TaskId"
    """<p>The task ID of the task that could not be updated.</p>"""
    code: "aws_sdk_deadline.types.batch_update_task_error_code.BatchUpdateTaskErrorCode"
    """<p>The error code.</p>"""
    message: "aws_sdk_deadline.types.string.String"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskError) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    out["taskId"] = value["task_id"]
    import aws_sdk_deadline.types.batch_update_task_error_code

    out["code"] = aws_sdk_deadline.types.batch_update_task_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateTaskError:
    out: BatchUpdateTaskError = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchUpdateTaskError.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchUpdateTaskError.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchUpdateTaskError.job_id required")
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("BatchUpdateTaskError.step_id required")
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("BatchUpdateTaskError.task_id required")
    if "code" in data:
        import aws_sdk_deadline.types.batch_update_task_error_code

        out["code"] = (
            aws_sdk_deadline.types.batch_update_task_error_code.deserialize_json(
                data["code"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateTaskError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchUpdateTaskError.message required")
    return out
