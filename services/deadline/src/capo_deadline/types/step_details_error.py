"""Generated from Smithy shape ``com.amazonaws.deadline#StepDetailsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.job_entity_error_code
    import capo_deadline.types.job_id
    import capo_deadline.types.step_id
    import capo_deadline.types.string


class StepDetailsError(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    code: "capo_deadline.types.job_entity_error_code.JobEntityErrorCode"
    """<p>The error code.</p>"""
    message: "capo_deadline.types.string.String"
    """<p>The error message detailing the error's cause.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepDetailsError) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    import capo_deadline.types.job_entity_error_code

    out["code"] = capo_deadline.types.job_entity_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StepDetailsError:
    out: StepDetailsError = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("StepDetailsError.job_id required")
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("StepDetailsError.step_id required")
    if "code" in data:
        import capo_deadline.types.job_entity_error_code

        out["code"] = capo_deadline.types.job_entity_error_code.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError("StepDetailsError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("StepDetailsError.message required")
    return out
