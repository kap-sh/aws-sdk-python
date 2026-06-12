"""Generated from Smithy shape ``com.amazonaws.connectcases#ChannelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.channel

ChannelList: TypeAlias = list["aws_sdk_connectcases.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelList) -> list:
    return list(value)


def deserialize_json(data: list) -> ChannelList:
    return list(data)
