"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Relationship``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.string


class Relationship(TypedDict):
    target_component_type_id: NotRequired[
        "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"
    ]
    """<p>The ID of the target component type associated with this relationship.</p>"""
    relationship_type: NotRequired["aws_sdk_iottwinmaker.types.string.String"]
    """<p>The type of the relationship.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Relationship) -> dict:
    out: dict = {}
    if "target_component_type_id" in value:
        out["targetComponentTypeId"] = value["target_component_type_id"]
    if "relationship_type" in value:
        out["relationshipType"] = value["relationship_type"]
    return out


def deserialize_json(data: dict) -> Relationship:
    out: Relationship = {}  # type: ignore[typeddict-item]
    if "targetComponentTypeId" in data:
        out["target_component_type_id"] = data["targetComponentTypeId"]
    if "relationshipType" in data:
        out["relationship_type"] = data["relationshipType"]
    return out
