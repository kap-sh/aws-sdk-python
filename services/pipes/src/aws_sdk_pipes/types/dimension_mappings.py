"""Generated from Smithy shape ``com.amazonaws.pipes#DimensionMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.dimension_mapping

DimensionMappings: TypeAlias = list[
    "aws_sdk_pipes.types.dimension_mapping.DimensionMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionMappings) -> list:
    import aws_sdk_pipes.types.dimension_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.dimension_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> DimensionMappings:
    import aws_sdk_pipes.types.dimension_mapping

    out: DimensionMappings = []
    for item in data:
        out.append(aws_sdk_pipes.types.dimension_mapping.deserialize_json(item))
    return out
