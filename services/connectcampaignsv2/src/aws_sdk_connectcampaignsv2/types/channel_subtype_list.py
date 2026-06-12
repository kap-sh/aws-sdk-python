"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ChannelSubtypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.channel_subtype

ChannelSubtypeList: TypeAlias = list[
    "aws_sdk_connectcampaignsv2.types.channel_subtype.ChannelSubtype"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSubtypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ChannelSubtypeList:
    return list(data)
