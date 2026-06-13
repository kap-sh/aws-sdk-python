"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ChannelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.channel_list_configuration

ChannelList: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.channel_list_configuration.ChannelListConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelList) -> list:
    import aws_sdk_mediapackagev2.types.channel_list_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.channel_list_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChannelList:
    import aws_sdk_mediapackagev2.types.channel_list_configuration

    out: ChannelList = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.channel_list_configuration.deserialize_json(
                item
            )
        )
    return out
