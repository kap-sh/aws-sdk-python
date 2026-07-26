"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfMessageResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.message_result

MapOfMessageResult: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string",
    "capo_pinpoint.types.message_result.MessageResult",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfMessageResult) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pinpoint.types.message_result

        out[key] = capo_pinpoint.types.message_result.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfMessageResult:
    out: MapOfMessageResult = {}
    for key, value in data.items():
        import capo_pinpoint.types.message_result

        out[key] = capo_pinpoint.types.message_result.deserialize_json(value)
    return out
