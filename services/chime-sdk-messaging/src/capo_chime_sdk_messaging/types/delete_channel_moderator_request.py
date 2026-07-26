"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DeleteChannelModeratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class DeleteChannelModeratorRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    channel_moderator_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the moderator being deleted.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelModeratorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelModeratorRequest:
    out: DeleteChannelModeratorRequest = {}  # type: ignore[typeddict-item]
    return out
