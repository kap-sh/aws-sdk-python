"""Generated from Smithy shape ``com.amazonaws.iot#DimensionNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.dimension_name

DimensionNames: TypeAlias = list["aws_sdk_iot.types.dimension_name.DimensionName"]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionNames) -> list:
    return list(value)


def deserialize_json(data: list) -> DimensionNames:
    return list(data)
