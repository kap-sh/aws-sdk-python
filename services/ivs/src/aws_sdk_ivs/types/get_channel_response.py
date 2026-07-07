"""Generated from Smithy shape ``com.amazonaws.ivs#GetChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel


class GetChannelResponse(TypedDict, closed=True):
    channel: NotRequired["aws_sdk_ivs.types.channel.Channel"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import aws_sdk_ivs.types.channel

        out["channel"] = aws_sdk_ivs.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> GetChannelResponse:
    out: GetChannelResponse = {}  # type: ignore[typeddict-item]
    if "channel" in data:
        import aws_sdk_ivs.types.channel

        out["channel"] = aws_sdk_ivs.types.channel.deserialize_json(data["channel"])
    return out
