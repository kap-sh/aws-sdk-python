"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteDevEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.uuid


class DeleteDevEnvironmentRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment you want to delete. To retrieve a list of Dev Environment IDs, use <a>ListDevEnvironments</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDevEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDevEnvironmentRequest:
    out: DeleteDevEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
