"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.property_mapping

PropertyMappings: TypeAlias = list[
    "capo_iotsitewise.types.property_mapping.PropertyMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyMappings) -> list:
    import capo_iotsitewise.types.property_mapping

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.property_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> PropertyMappings:
    import capo_iotsitewise.types.property_mapping

    out: PropertyMappings = []
    for item in data:
        out.append(capo_iotsitewise.types.property_mapping.deserialize_json(item))
    return out
