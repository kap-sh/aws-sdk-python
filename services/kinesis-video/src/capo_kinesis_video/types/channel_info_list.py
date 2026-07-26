"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ChannelInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_video.types.channel_info

ChannelInfoList: TypeAlias = list["capo_kinesis_video.types.channel_info.ChannelInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelInfoList) -> list:
    import capo_kinesis_video.types.channel_info

    out: list = []
    for item in value:
        out.append(capo_kinesis_video.types.channel_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChannelInfoList:
    import capo_kinesis_video.types.channel_info

    out: ChannelInfoList = []
    for item in data:
        out.append(capo_kinesis_video.types.channel_info.deserialize_json(item))
    return out
