"""Generated from Smithy shape ``com.amazonaws.databrew#StartProjectSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.client_session_id
    import capo_databrew.types.project_name


class StartProjectSessionResponse(TypedDict, closed=True):
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>The name of the project to be acted upon.</p>"""
    client_session_id: NotRequired[
        "capo_databrew.types.client_session_id.ClientSessionId"
    ]
    """<p>A system-generated identifier for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProjectSessionResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_session_id" in value:
        out["ClientSessionId"] = value["client_session_id"]
    return out


def deserialize_json(data: dict) -> StartProjectSessionResponse:
    out: StartProjectSessionResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartProjectSessionResponse.name required")
    if "ClientSessionId" in data:
        out["client_session_id"] = data["ClientSessionId"]
    return out
