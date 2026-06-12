"""Generated from Smithy shape ``com.amazonaws.ivs#ChannelArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_arn

ChannelArnList: TypeAlias = list["aws_sdk_ivs.types.channel_arn.ChannelArn"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ChannelArnList:
    return list(data)
