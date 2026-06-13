"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ChannelGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.channel_group_list_configuration

ChannelGroupsList: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.channel_group_list_configuration.ChannelGroupListConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelGroupsList) -> list:
    import aws_sdk_mediapackagev2.types.channel_group_list_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.channel_group_list_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChannelGroupsList:
    import aws_sdk_mediapackagev2.types.channel_group_list_configuration

    out: ChannelGroupsList = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.channel_group_list_configuration.deserialize_json(
                item
            )
        )
    return out
