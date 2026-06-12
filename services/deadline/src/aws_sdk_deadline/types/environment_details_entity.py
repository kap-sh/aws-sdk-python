"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentDetailsEntity``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.document
    import aws_sdk_deadline.types.environment_id
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.string


class EnvironmentDetailsEntity(TypedDict):
    job_id: "aws_sdk_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    environment_id: "aws_sdk_deadline.types.environment_id.EnvironmentId"
    """<p>The environment ID.</p>"""
    schema_version: "aws_sdk_deadline.types.string.String"
    """<p>The schema version in the environment.</p>"""
    template: "aws_sdk_deadline.types.document.Document"
    """<p>The template used for the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentDetailsEntity) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["environmentId"] = value["environment_id"]
    out["schemaVersion"] = value["schema_version"]
    out["template"] = value["template"]
    return out


def deserialize_json(data: dict) -> EnvironmentDetailsEntity:
    out: EnvironmentDetailsEntity = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("EnvironmentDetailsEntity.job_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("EnvironmentDetailsEntity.environment_id required")
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("EnvironmentDetailsEntity.schema_version required")
    if "template" in data:
        out["template"] = data["template"]
    else:
        raise DeserializationError("EnvironmentDetailsEntity.template required")
    return out
