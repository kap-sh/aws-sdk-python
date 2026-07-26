"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Channels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.channel

Channels: TypeAlias = list["capo_codeguruprofiler.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: Channels) -> list:
    import capo_codeguruprofiler.types.channel

    out: list = []
    for item in value:
        out.append(capo_codeguruprofiler.types.channel.serialize_json(item))
    return out


def deserialize_json(data: list) -> Channels:
    import capo_codeguruprofiler.types.channel

    out: Channels = []
    for item in data:
        out.append(capo_codeguruprofiler.types.channel.deserialize_json(item))
    return out
