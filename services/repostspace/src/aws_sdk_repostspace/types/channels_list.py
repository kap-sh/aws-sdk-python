"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.channel_data

ChannelsList: TypeAlias = list["aws_sdk_repostspace.types.channel_data.ChannelData"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelsList) -> list:
    import aws_sdk_repostspace.types.channel_data

    out: list = []
    for item in value:
        out.append(aws_sdk_repostspace.types.channel_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChannelsList:
    import aws_sdk_repostspace.types.channel_data

    out: ChannelsList = []
    for item in data:
        out.append(aws_sdk_repostspace.types.channel_data.deserialize_json(item))
    return out
