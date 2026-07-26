"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.entity_id
    import capo_iottwinmaker.types.id


class GetEntityRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    entity_id: "capo_iottwinmaker.types.entity_id.EntityId"
    """<p>The ID of the entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEntityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEntityRequest:
    out: GetEntityRequest = {}  # type: ignore[typeddict-item]
    return out
