"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetSceneRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id


class GetSceneRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the scene.</p>"""
    scene_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the scene.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSceneRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSceneRequest:
    out: GetSceneRequest = {}  # type: ignore[typeddict-item]
    return out
