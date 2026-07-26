"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#StreamInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_video.types.stream_info

StreamInfoList: TypeAlias = list["capo_kinesis_video.types.stream_info.StreamInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamInfoList) -> list:
    import capo_kinesis_video.types.stream_info

    out: list = []
    for item in value:
        out.append(capo_kinesis_video.types.stream_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamInfoList:
    import capo_kinesis_video.types.stream_info

    out: StreamInfoList = []
    for item in data:
        out.append(capo_kinesis_video.types.stream_info.deserialize_json(item))
    return out
