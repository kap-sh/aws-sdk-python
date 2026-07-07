"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.id


class DeleteEntityRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the entity to delete.</p>"""
    entity_id: "aws_sdk_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID of the entity to delete.</p>"""
    is_recursive: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value that specifies whether the operation deletes child entities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEntityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEntityRequest:
    out: DeleteEntityRequest = {}  # type: ignore[typeddict-item]
    return out
