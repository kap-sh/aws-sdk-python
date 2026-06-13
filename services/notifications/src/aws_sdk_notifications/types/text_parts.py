"""Generated from Smithy shape ``com.amazonaws.notifications#TextParts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notifications.types.text_part_id
    import aws_sdk_notifications.types.text_part_value

TextParts: TypeAlias = dict[
    "aws_sdk_notifications.types.text_part_id.TextPartId",
    "aws_sdk_notifications.types.text_part_value.TextPartValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TextParts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_notifications.types.text_part_value

        out[key] = aws_sdk_notifications.types.text_part_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TextParts:
    out: TextParts = {}
    for key, value in data.items():
        import aws_sdk_notifications.types.text_part_value

        out[key] = aws_sdk_notifications.types.text_part_value.deserialize_json(value)
    return out
