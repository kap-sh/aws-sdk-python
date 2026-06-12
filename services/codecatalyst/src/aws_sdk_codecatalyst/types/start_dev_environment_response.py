"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StartDevEnvironmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.dev_environment_status
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.uuid


class StartDevEnvironmentResponse(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment. </p>"""
    status: "aws_sdk_codecatalyst.types.dev_environment_status.DevEnvironmentStatus"
    """<p>The status of the Dev Environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDevEnvironmentResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> StartDevEnvironmentResponse:
    out: StartDevEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("StartDevEnvironmentResponse.space_name required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("StartDevEnvironmentResponse.project_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartDevEnvironmentResponse.id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("StartDevEnvironmentResponse.status required")
    return out
