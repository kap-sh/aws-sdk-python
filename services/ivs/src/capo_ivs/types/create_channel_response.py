"""Generated from Smithy shape ``com.amazonaws.ivs#CreateChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel
    import capo_ivs.types.stream_key


class CreateChannelResponse(TypedDict, closed=True):
    channel: NotRequired["capo_ivs.types.channel.Channel"]
    """<p/>"""
    stream_key: NotRequired["capo_ivs.types.stream_key.StreamKey"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import capo_ivs.types.channel

        out["channel"] = capo_ivs.types.channel.serialize_json(value["channel"])
    if "stream_key" in value:
        import capo_ivs.types.stream_key

        out["streamKey"] = capo_ivs.types.stream_key.serialize_json(value["stream_key"])
    return out


def deserialize_json(data: dict) -> CreateChannelResponse:
    out: CreateChannelResponse = {}  # type: ignore[typeddict-item]
    if "channel" in data:
        import capo_ivs.types.channel

        out["channel"] = capo_ivs.types.channel.deserialize_json(data["channel"])
    if "streamKey" in data:
        import capo_ivs.types.stream_key

        out["stream_key"] = capo_ivs.types.stream_key.deserialize_json(
            data["streamKey"]
        )
    return out
