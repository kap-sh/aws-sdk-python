"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ChannelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.channel_list_configuration

ChannelList: TypeAlias = list[
    "capo_mediapackagev2.types.channel_list_configuration.ChannelListConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelList) -> list:
    import capo_mediapackagev2.types.channel_list_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.channel_list_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChannelList:
    import capo_mediapackagev2.types.channel_list_configuration

    out: ChannelList = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.channel_list_configuration.deserialize_json(item)
        )
    return out
