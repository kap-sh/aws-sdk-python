"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel


class DescribeChannelResponse(TypedDict, closed=True):
    channel: NotRequired["capo_chime_sdk_messaging.types.channel.Channel"]
    """<p>The channel details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import capo_chime_sdk_messaging.types.channel

        out["Channel"] = capo_chime_sdk_messaging.types.channel.serialize_json(
            value["channel"]
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelResponse:
    out: DescribeChannelResponse = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        import capo_chime_sdk_messaging.types.channel

        out["channel"] = capo_chime_sdk_messaging.types.channel.deserialize_json(
            data["Channel"]
        )
    return out
