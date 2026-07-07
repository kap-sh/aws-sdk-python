"""Generated from Smithy shape ``com.amazonaws.deadline#StepDetailsIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.step_id


class StepDetailsIdentifiers(TypedDict, closed=True):
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    step_id: "aws_sdk_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepDetailsIdentifiers) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    return out


def deserialize_json(data: dict) -> StepDetailsIdentifiers:
    out: StepDetailsIdentifiers = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("StepDetailsIdentifiers.job_id required")
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("StepDetailsIdentifiers.step_id required")
    return out
