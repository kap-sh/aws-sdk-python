"""Generated from Smithy shape ``com.amazonaws.iot#DimensionStringValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.dimension_string_value

DimensionStringValues: TypeAlias = list[
    "aws_sdk_iot.types.dimension_string_value.DimensionStringValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionStringValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DimensionStringValues:
    return list(data)
