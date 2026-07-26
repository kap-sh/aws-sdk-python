"""Generated from Smithy shape ``com.amazonaws.networkmanager#RelationshipList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.relationship

RelationshipList: TypeAlias = list[
    "capo_networkmanager.types.relationship.Relationship"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelationshipList) -> list:
    import capo_networkmanager.types.relationship

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.relationship.serialize_json(item))
    return out


def deserialize_json(data: list) -> RelationshipList:
    import capo_networkmanager.types.relationship

    out: RelationshipList = []
    for item in data:
        out.append(capo_networkmanager.types.relationship.deserialize_json(item))
    return out
