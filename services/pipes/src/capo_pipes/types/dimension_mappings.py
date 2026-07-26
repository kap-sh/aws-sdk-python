"""Generated from Smithy shape ``com.amazonaws.pipes#DimensionMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.dimension_mapping

DimensionMappings: TypeAlias = list[
    "capo_pipes.types.dimension_mapping.DimensionMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionMappings) -> list:
    import capo_pipes.types.dimension_mapping

    out: list = []
    for item in value:
        out.append(capo_pipes.types.dimension_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> DimensionMappings:
    import capo_pipes.types.dimension_mapping

    out: DimensionMappings = []
    for item in data:
        out.append(capo_pipes.types.dimension_mapping.deserialize_json(item))
    return out
