"""Generated from Smithy shape ``com.amazonaws.ivs#Channels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel

Channels: TypeAlias = list["aws_sdk_ivs.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: Channels) -> list:
    import aws_sdk_ivs.types.channel

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs.types.channel.serialize_json(item))
    return out


def deserialize_json(data: list) -> Channels:
    import aws_sdk_ivs.types.channel

    out: Channels = []
    for item in data:
        out.append(aws_sdk_ivs.types.channel.deserialize_json(item))
    return out
