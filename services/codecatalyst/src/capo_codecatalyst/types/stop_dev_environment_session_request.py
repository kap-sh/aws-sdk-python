"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StopDevEnvironmentSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.uuid


class StopDevEnvironmentSessionRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment. To obtain this ID, use <a>ListDevEnvironments</a>.</p>"""
    session_id: "str"
    """<p>The system-generated unique ID of the Dev Environment session. This ID is returned by <a>StartDevEnvironmentSession</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDevEnvironmentSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopDevEnvironmentSessionRequest:
    out: StopDevEnvironmentSessionRequest = {}  # type: ignore[typeddict-item]
    return out
