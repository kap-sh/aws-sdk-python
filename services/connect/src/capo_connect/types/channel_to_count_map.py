"""Generated from Smithy shape ``com.amazonaws.connect#ChannelToCountMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.channel
    import capo_connect.types.integer_count

ChannelToCountMap: TypeAlias = dict[
    "capo_connect.types.channel.Channel",
    "capo_connect.types.integer_count.IntegerCount",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ChannelToCountMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connect.types.channel

        out[capo_connect.types.channel.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> ChannelToCountMap:
    out: ChannelToCountMap = {}
    for key, value in data.items():
        import capo_connect.types.channel

        out[capo_connect.types.channel.deserialize_json(key)] = value
    return out
