"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StartDevEnvironmentSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.dev_environment_access_details
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.uuid


class StartDevEnvironmentSessionResponse(TypedDict, closed=True):
    access_details: "capo_codecatalyst.types.dev_environment_access_details.DevEnvironmentAccessDetails"
    session_id: NotRequired["str"]
    """<p>The system-generated unique ID of the Dev Environment session.</p>"""
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDevEnvironmentSessionResponse) -> dict:
    out: dict = {}
    import capo_codecatalyst.types.dev_environment_access_details

    out["accessDetails"] = (
        capo_codecatalyst.types.dev_environment_access_details.serialize_json(
            value["access_details"]
        )
    )
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> StartDevEnvironmentSessionResponse:
    out: StartDevEnvironmentSessionResponse = {}  # type: ignore[typeddict-item]
    if "accessDetails" in data:
        import capo_codecatalyst.types.dev_environment_access_details

        out["access_details"] = (
            capo_codecatalyst.types.dev_environment_access_details.deserialize_json(
                data["accessDetails"]
            )
        )
    else:
        raise DeserializationError(
            "StartDevEnvironmentSessionResponse.access_details required"
        )
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError(
            "StartDevEnvironmentSessionResponse.space_name required"
        )
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError(
            "StartDevEnvironmentSessionResponse.project_name required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartDevEnvironmentSessionResponse.id required")
    return out
