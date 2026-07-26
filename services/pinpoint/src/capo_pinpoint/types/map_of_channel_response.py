"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfChannelResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.channel_response

MapOfChannelResponse: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string",
    "capo_pinpoint.types.channel_response.ChannelResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfChannelResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pinpoint.types.channel_response

        out[key] = capo_pinpoint.types.channel_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfChannelResponse:
    out: MapOfChannelResponse = {}
    for key, value in data.items():
        import capo_pinpoint.types.channel_response

        out[key] = capo_pinpoint.types.channel_response.deserialize_json(value)
    return out
