"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelReadMarkerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class UpdateChannelReadMarkerResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelReadMarkerResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    return out


def deserialize_json(data: dict) -> UpdateChannelReadMarkerResponse:
    out: UpdateChannelReadMarkerResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    return out
