"""Generated from Smithy shape ``com.amazonaws.connect#Channels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.channel

Channels: TypeAlias = list["capo_connect.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: Channels) -> list:
    import capo_connect.types.channel

    out: list = []
    for item in value:
        out.append(capo_connect.types.channel.serialize_json(item))
    return out


def deserialize_json(data: list) -> Channels:
    import capo_connect.types.channel

    out: Channels = []
    for item in data:
        out.append(capo_connect.types.channel.deserialize_json(item))
    return out
