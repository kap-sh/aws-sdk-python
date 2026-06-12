"""Generated from Smithy shape ``com.amazonaws.iot#StreamFiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.stream_file

StreamFiles: TypeAlias = list["aws_sdk_iot.types.stream_file.StreamFile"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamFiles) -> list:
    import aws_sdk_iot.types.stream_file

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.stream_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamFiles:
    import aws_sdk_iot.types.stream_file

    out: StreamFiles = []
    for item in data:
        out.append(aws_sdk_iot.types.stream_file.deserialize_json(item))
    return out
