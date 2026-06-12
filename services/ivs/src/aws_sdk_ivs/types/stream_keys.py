"""Generated from Smithy shape ``com.amazonaws.ivs#StreamKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.stream_key

StreamKeys: TypeAlias = list["aws_sdk_ivs.types.stream_key.StreamKey"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamKeys) -> list:
    import aws_sdk_ivs.types.stream_key

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs.types.stream_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamKeys:
    import aws_sdk_ivs.types.stream_key

    out: StreamKeys = []
    for item in data:
        out.append(aws_sdk_ivs.types.stream_key.deserialize_json(item))
    return out
