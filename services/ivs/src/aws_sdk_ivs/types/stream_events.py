"""Generated from Smithy shape ``com.amazonaws.ivs#StreamEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.stream_event

StreamEvents: TypeAlias = list["aws_sdk_ivs.types.stream_event.StreamEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamEvents) -> list:
    import aws_sdk_ivs.types.stream_event

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs.types.stream_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamEvents:
    import aws_sdk_ivs.types.stream_event

    out: StreamEvents = []
    for item in data:
        out.append(aws_sdk_ivs.types.stream_event.deserialize_json(item))
    return out
