"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InterfaceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.interface_relationship

InterfaceDetails: TypeAlias = list[
    "capo_iotsitewise.types.interface_relationship.InterfaceRelationship"
]


# --- restJson1 ser/de ---
def serialize_json(value: InterfaceDetails) -> list:
    import capo_iotsitewise.types.interface_relationship

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.interface_relationship.serialize_json(item))
    return out


def deserialize_json(data: list) -> InterfaceDetails:
    import capo_iotsitewise.types.interface_relationship

    out: InterfaceDetails = []
    for item in data:
        out.append(capo_iotsitewise.types.interface_relationship.deserialize_json(item))
    return out
