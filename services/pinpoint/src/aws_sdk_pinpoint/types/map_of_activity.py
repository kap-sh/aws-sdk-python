"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfActivity``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.activity

MapOfActivity: TypeAlias = dict[
    "aws_sdk_pinpoint.types.__string.__string",
    "aws_sdk_pinpoint.types.activity.Activity",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfActivity) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_pinpoint.types.activity

        out[key] = aws_sdk_pinpoint.types.activity.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfActivity:
    out: MapOfActivity = {}
    for key, value in data.items():
        import aws_sdk_pinpoint.types.activity

        out[key] = aws_sdk_pinpoint.types.activity.deserialize_json(value)
    return out
