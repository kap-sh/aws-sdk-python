"""Generated from Smithy shape ``com.amazonaws.ivs#ChannelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_summary

ChannelList: TypeAlias = list["aws_sdk_ivs.types.channel_summary.ChannelSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelList) -> list:
    import aws_sdk_ivs.types.channel_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs.types.channel_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChannelList:
    import aws_sdk_ivs.types.channel_summary

    out: ChannelList = []
    for item in data:
        out.append(aws_sdk_ivs.types.channel_summary.deserialize_json(item))
    return out
