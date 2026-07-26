"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StopDevEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.dev_environment_status
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.uuid


class StopDevEnvironmentResponse(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment. </p>"""
    status: "capo_codecatalyst.types.dev_environment_status.DevEnvironmentStatus"
    """<p>The status of the Dev Environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDevEnvironmentResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> StopDevEnvironmentResponse:
    out: StopDevEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("StopDevEnvironmentResponse.space_name required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("StopDevEnvironmentResponse.project_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StopDevEnvironmentResponse.id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("StopDevEnvironmentResponse.status required")
    return out
