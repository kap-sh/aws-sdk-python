"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOf__double``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__double
    import aws_sdk_pinpoint.types.__string

MapOf__double: TypeAlias = dict[
    "aws_sdk_pinpoint.types.__string.__string",
    "aws_sdk_pinpoint.types.__double.__double",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOf__double) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MapOf__double:
    out: MapOf__double = {}
    for key, value in data.items():
        out[key] = value
    return out
