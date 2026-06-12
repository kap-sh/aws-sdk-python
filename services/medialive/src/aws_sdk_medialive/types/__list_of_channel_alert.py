"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfChannelAlert``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.channel_alert

__listOfChannelAlert: TypeAlias = list[
    "aws_sdk_medialive.types.channel_alert.ChannelAlert"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannelAlert) -> list:
    import aws_sdk_medialive.types.channel_alert

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.channel_alert.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfChannelAlert:
    import aws_sdk_medialive.types.channel_alert

    out: __listOfChannelAlert = []
    for item in data:
        out.append(aws_sdk_medialive.types.channel_alert.deserialize_json(item))
    return out
