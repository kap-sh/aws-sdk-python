"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfAttributeDimension``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.attribute_dimension

MapOfAttributeDimension: TypeAlias = dict[
    "aws_sdk_pinpoint.types.__string.__string",
    "aws_sdk_pinpoint.types.attribute_dimension.AttributeDimension",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfAttributeDimension) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_pinpoint.types.attribute_dimension

        out[key] = aws_sdk_pinpoint.types.attribute_dimension.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfAttributeDimension:
    out: MapOfAttributeDimension = {}
    for key, value in data.items():
        import aws_sdk_pinpoint.types.attribute_dimension

        out[key] = aws_sdk_pinpoint.types.attribute_dimension.deserialize_json(value)
    return out
