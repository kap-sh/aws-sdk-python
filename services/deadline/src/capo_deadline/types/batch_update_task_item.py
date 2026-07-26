"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.step_id
    import capo_deadline.types.task_id
    import capo_deadline.types.task_target_run_status


class BatchUpdateTaskItem(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the task to update.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the task to update.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID of the task to update.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID of the task to update.</p>"""
    task_id: "capo_deadline.types.task_id.TaskId"
    """<p>The task ID of the task to update.</p>"""
    target_run_status: "capo_deadline.types.task_target_run_status.TaskTargetRunStatus"
    """<p>The run status with which to start the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    out["taskId"] = value["task_id"]
    import capo_deadline.types.task_target_run_status

    out["targetRunStatus"] = capo_deadline.types.task_target_run_status.serialize_json(
        value["target_run_status"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateTaskItem:
    out: BatchUpdateTaskItem = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchUpdateTaskItem.farm_id required")
    if "queueId" in data:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchUpdateTaskItem.queue_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchUpdateTaskItem.job_id required")
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("BatchUpdateTaskItem.step_id required")
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("BatchUpdateTaskItem.task_id required")
    if "targetRunStatus" in data:
        import capo_deadline.types.task_target_run_status

        out["target_run_status"] = (
            capo_deadline.types.task_target_run_status.deserialize_json(
                data["targetRunStatus"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateTaskItem.target_run_status required")
    return out
