"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StopDevEnvironmentSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.uuid


class StopDevEnvironmentSessionResponse(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment.</p>"""
    session_id: "str"
    """<p>The system-generated unique ID of the Dev Environment session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDevEnvironmentSessionResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> StopDevEnvironmentSessionResponse:
    out: StopDevEnvironmentSessionResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError(
            "StopDevEnvironmentSessionResponse.space_name required"
        )
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError(
            "StopDevEnvironmentSessionResponse.project_name required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StopDevEnvironmentSessionResponse.id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError(
            "StopDevEnvironmentSessionResponse.session_id required"
        )
    return out
