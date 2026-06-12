"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfChannel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.channel

__listOfChannel: TypeAlias = list["aws_sdk_mediatailor.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannel) -> list:
    import aws_sdk_mediatailor.types.channel

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.channel.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfChannel:
    import aws_sdk_mediatailor.types.channel

    out: __listOfChannel = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.channel.deserialize_json(item))
    return out
