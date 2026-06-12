"""Generated from Smithy shape ``com.amazonaws.connect#ChannelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.channel

ChannelList: TypeAlias = list["aws_sdk_connect.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelList) -> list:
    import aws_sdk_connect.types.channel

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.channel.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChannelList:
    import aws_sdk_connect.types.channel

    out: ChannelList = []
    for item in data:
        out.append(aws_sdk_connect.types.channel.deserialize_json(item))
    return out
