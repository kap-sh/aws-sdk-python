"""Generated from Smithy shape ``com.amazonaws.deadline#GetStepRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.step_id


class GetStepRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the step.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the step.</p>"""
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID for the step.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStepRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStepRequest:
    out: GetStepRequest = {}  # type: ignore[typeddict-item]
    return out
