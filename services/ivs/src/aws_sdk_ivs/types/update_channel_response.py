"""Generated from Smithy shape ``com.amazonaws.ivs#UpdateChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel


class UpdateChannelResponse(TypedDict, closed=True):
    channel: NotRequired["aws_sdk_ivs.types.channel.Channel"]
    """<p>Object specifying the updated channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import aws_sdk_ivs.types.channel

        out["channel"] = aws_sdk_ivs.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> UpdateChannelResponse:
    out: UpdateChannelResponse = {}  # type: ignore[typeddict-item]
    if "channel" in data:
        import aws_sdk_ivs.types.channel

        out["channel"] = aws_sdk_ivs.types.channel.deserialize_json(data["channel"])
    return out
