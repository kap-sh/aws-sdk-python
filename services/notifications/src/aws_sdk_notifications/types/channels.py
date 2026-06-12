"""Generated from Smithy shape ``com.amazonaws.notifications#Channels``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_notifications.types.channel_arn

Channels: TypeAlias = list["aws_sdk_notifications.types.channel_arn.ChannelArn"]


# --- restJson1 ser/de ---
def serialize_json(value: Channels) -> list:
    return list(value)


def deserialize_json(data: list) -> Channels:
    return list(data)