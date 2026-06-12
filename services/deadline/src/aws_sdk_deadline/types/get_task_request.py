"""Generated from Smithy shape ``com.amazonaws.deadline#GetTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.step_id
    import aws_sdk_deadline.types.task_id


class GetTaskRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm connected to the task.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the queue connected to the task.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID of the job connected to the task.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID for the step connected to the task.</p>"""
    task_id: "aws_sdk_deadline.types.task_id.TaskId"
    """<p>The task ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTaskRequest:
    out: GetTaskRequest = {}  # type: ignore[typeddict-item]
    return out
