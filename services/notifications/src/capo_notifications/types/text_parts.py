"""Generated from Smithy shape ``com.amazonaws.notifications#TextParts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.text_part_id
    import capo_notifications.types.text_part_value

TextParts: TypeAlias = dict[
    "capo_notifications.types.text_part_id.TextPartId",
    "capo_notifications.types.text_part_value.TextPartValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TextParts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_notifications.types.text_part_value

        out[key] = capo_notifications.types.text_part_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TextParts:
    out: TextParts = {}
    for key, value in data.items():
        import capo_notifications.types.text_part_value

        out[key] = capo_notifications.types.text_part_value.deserialize_json(value)
    return out
