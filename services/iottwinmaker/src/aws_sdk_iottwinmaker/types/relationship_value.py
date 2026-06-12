"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#RelationshipValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.entity_id
    import aws_sdk_iottwinmaker.types.name


class RelationshipValue(TypedDict):
    target_entity_id: NotRequired["aws_sdk_iottwinmaker.types.entity_id.EntityId"]
    """<p>The ID of the target entity associated with this relationship value.</p>"""
    target_component_name: NotRequired["aws_sdk_iottwinmaker.types.name.Name"]
    """<p>The name of the target component associated with the relationship value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelationshipValue) -> dict:
    out: dict = {}
    if "target_entity_id" in value:
        out["targetEntityId"] = value["target_entity_id"]
    if "target_component_name" in value:
        out["targetComponentName"] = value["target_component_name"]
    return out


def deserialize_json(data: dict) -> RelationshipValue:
    out: RelationshipValue = {}  # type: ignore[typeddict-item]
    if "targetEntityId" in data:
        out["target_entity_id"] = data["targetEntityId"]
    if "targetComponentName" in data:
        out["target_component_name"] = data["targetComponentName"]
    return out
