"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteSceneRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id


class DeleteSceneRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    scene_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the scene to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSceneRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSceneRequest:
    out: DeleteSceneRequest = {}  # type: ignore[typeddict-item]
    return out
