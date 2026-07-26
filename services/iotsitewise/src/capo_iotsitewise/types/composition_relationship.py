"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CompositionRelationship``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.composition_relationship_item

CompositionRelationship: TypeAlias = list[
    "capo_iotsitewise.types.composition_relationship_item.CompositionRelationshipItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompositionRelationship) -> list:
    import capo_iotsitewise.types.composition_relationship_item

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.composition_relationship_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CompositionRelationship:
    import capo_iotsitewise.types.composition_relationship_item

    out: CompositionRelationship = []
    for item in data:
        out.append(
            capo_iotsitewise.types.composition_relationship_item.deserialize_json(item)
        )
    return out
