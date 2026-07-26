"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UpdateChannelReadMarkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class UpdateChannelReadMarkerRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelReadMarkerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UpdateChannelReadMarkerRequest:
    out: UpdateChannelReadMarkerRequest = {}  # type: ignore[typeddict-item]
    return out
