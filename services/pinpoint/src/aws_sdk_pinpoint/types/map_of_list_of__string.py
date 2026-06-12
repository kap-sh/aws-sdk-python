"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfListOf__string``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.list_of__string

MapOfListOf__string: TypeAlias = dict[
    "aws_sdk_pinpoint.types.__string.__string",
    "aws_sdk_pinpoint.types.list_of__string.ListOf__string",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfListOf__string) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_pinpoint.types.list_of__string

        out[key] = aws_sdk_pinpoint.types.list_of__string.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfListOf__string:
    out: MapOfListOf__string = {}
    for key, value in data.items():
        import aws_sdk_pinpoint.types.list_of__string

        out[key] = aws_sdk_pinpoint.types.list_of__string.deserialize_json(value)
    return out
