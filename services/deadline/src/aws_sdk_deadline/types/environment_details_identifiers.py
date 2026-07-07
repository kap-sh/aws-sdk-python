"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentDetailsIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.environment_id
    import aws_sdk_deadline.types.job_id


class EnvironmentDetailsIdentifiers(TypedDict, closed=True):
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    environment_id: "aws_sdk_deadline.types.environment_id.EnvironmentId"
    """<p>The environment ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentDetailsIdentifiers) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_json(data: dict) -> EnvironmentDetailsIdentifiers:
    out: EnvironmentDetailsIdentifiers = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("EnvironmentDetailsIdentifiers.job_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "EnvironmentDetailsIdentifiers.environment_id required"
        )
    return out
