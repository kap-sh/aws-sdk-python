"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfEventItemResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.event_item_response

MapOfEventItemResponse: TypeAlias = dict[
    "aws_sdk_pinpoint.types.__string.__string",
    "aws_sdk_pinpoint.types.event_item_response.EventItemResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfEventItemResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_pinpoint.types.event_item_response

        out[key] = aws_sdk_pinpoint.types.event_item_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfEventItemResponse:
    out: MapOfEventItemResponse = {}
    for key, value in data.items():
        import aws_sdk_pinpoint.types.event_item_response

        out[key] = aws_sdk_pinpoint.types.event_item_response.deserialize_json(value)
    return out
