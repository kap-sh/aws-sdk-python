"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ChannelGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.channel_group_list_configuration

ChannelGroupsList: TypeAlias = list[
    "capo_mediapackagev2.types.channel_group_list_configuration.ChannelGroupListConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelGroupsList) -> list:
    import capo_mediapackagev2.types.channel_group_list_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.channel_group_list_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChannelGroupsList:
    import capo_mediapackagev2.types.channel_group_list_configuration

    out: ChannelGroupsList = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.channel_group_list_configuration.deserialize_json(
                item
            )
        )
    return out
