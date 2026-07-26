"""Generated from Smithy shape ``com.amazonaws.qconnect#Channels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.channel

Channels: TypeAlias = list["capo_qconnect.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: Channels) -> list:
    return list(value)


def deserialize_json(data: list) -> Channels:
    return list(data)
