"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteDevEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.uuid


class DeleteDevEnvironmentResponse(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the deleted Dev Environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDevEnvironmentResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeleteDevEnvironmentResponse:
    out: DeleteDevEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("DeleteDevEnvironmentResponse.space_name required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("DeleteDevEnvironmentResponse.project_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteDevEnvironmentResponse.id required")
    return out
