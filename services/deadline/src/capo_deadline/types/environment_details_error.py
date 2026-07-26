"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentDetailsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.environment_id
    import capo_deadline.types.job_entity_error_code
    import capo_deadline.types.job_id
    import capo_deadline.types.string


class EnvironmentDetailsError(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    environment_id: "capo_deadline.types.environment_id.EnvironmentId"
    """<p>The environment ID.</p>"""
    code: "capo_deadline.types.job_entity_error_code.JobEntityErrorCode"
    """<p>The error code.</p>"""
    message: "capo_deadline.types.string.String"
    """<p>The error message detailing the error's cause.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentDetailsError) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["environmentId"] = value["environment_id"]
    import capo_deadline.types.job_entity_error_code

    out["code"] = capo_deadline.types.job_entity_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EnvironmentDetailsError:
    out: EnvironmentDetailsError = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("EnvironmentDetailsError.job_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("EnvironmentDetailsError.environment_id required")
    if "code" in data:
        import capo_deadline.types.job_entity_error_code

        out["code"] = capo_deadline.types.job_entity_error_code.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError("EnvironmentDetailsError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("EnvironmentDetailsError.message required")
    return out
