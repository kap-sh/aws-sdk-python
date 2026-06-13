"""Generated from Smithy shape ``com.amazonaws.location#MultiLinearRings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.linear_rings

MultiLinearRings: TypeAlias = list["aws_sdk_location.types.linear_rings.LinearRings"]


# --- restJson1 ser/de ---
def serialize_json(value: MultiLinearRings) -> list:
    import aws_sdk_location.types.linear_rings

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.linear_rings.serialize_json(item))
    return out


def deserialize_json(data: list) -> MultiLinearRings:
    import aws_sdk_location.types.linear_rings

    out: MultiLinearRings = []
    for item in data:
        out.append(aws_sdk_location.types.linear_rings.deserialize_json(item))
    return out
