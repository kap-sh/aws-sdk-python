"""Generated from Smithy shape ``com.amazonaws.wisdom#Channels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.channel

Channels: TypeAlias = list["capo_wisdom.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: Channels) -> list:
    return list(value)


def deserialize_json(data: list) -> Channels:
    return list(data)
