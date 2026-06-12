"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfEventsBatch``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.events_batch

MapOfEventsBatch: TypeAlias = dict[
    "aws_sdk_pinpoint.types.__string.__string",
    "aws_sdk_pinpoint.types.events_batch.EventsBatch",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfEventsBatch) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_pinpoint.types.events_batch

        out[key] = aws_sdk_pinpoint.types.events_batch.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfEventsBatch:
    out: MapOfEventsBatch = {}
    for key, value in data.items():
        import aws_sdk_pinpoint.types.events_batch

        out[key] = aws_sdk_pinpoint.types.events_batch.deserialize_json(value)
    return out
