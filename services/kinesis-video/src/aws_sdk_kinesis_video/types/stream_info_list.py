"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#StreamInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.stream_info

StreamInfoList: TypeAlias = list["aws_sdk_kinesis_video.types.stream_info.StreamInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamInfoList) -> list:
    import aws_sdk_kinesis_video.types.stream_info

    out: list = []
    for item in value:
        out.append(aws_sdk_kinesis_video.types.stream_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamInfoList:
    import aws_sdk_kinesis_video.types.stream_info

    out: StreamInfoList = []
    for item in data:
        out.append(aws_sdk_kinesis_video.types.stream_info.deserialize_json(item))
    return out
