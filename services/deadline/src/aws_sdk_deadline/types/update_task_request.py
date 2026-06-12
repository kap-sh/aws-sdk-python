"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.step_id
    import aws_sdk_deadline.types.task_id
    import aws_sdk_deadline.types.task_target_run_status


class UpdateTaskRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID to update.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID to update.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID to update.</p>"""
    task_id: "aws_sdk_deadline.types.task_id.TaskId"
    """<p>The task ID to update.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    target_run_status: (
        "aws_sdk_deadline.types.task_target_run_status.TaskTargetRunStatus"
    )
    """<p>The run status with which to start the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTaskRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.task_target_run_status

    out["targetRunStatus"] = (
        aws_sdk_deadline.types.task_target_run_status.serialize_json(
            value["target_run_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTaskRequest:
    out: UpdateTaskRequest = {}  # type: ignore[typeddict-item]
    if "targetRunStatus" in data:
        import aws_sdk_deadline.types.task_target_run_status

        out["target_run_status"] = (
            aws_sdk_deadline.types.task_target_run_status.deserialize_json(
                data["targetRunStatus"]
            )
        )
    else:
        raise DeserializationError("UpdateTaskRequest.target_run_status required")
    return out
