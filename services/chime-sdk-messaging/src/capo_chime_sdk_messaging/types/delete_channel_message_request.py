"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DeleteChannelMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.message_id
    import capo_chime_sdk_messaging.types.sub_channel_id


class DeleteChannelMessageRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    message_id: "capo_chime_sdk_messaging.types.message_id.MessageId"
    """<p>The ID of the message being deleted.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p> <note> <p>Only required when deleting messages in a SubChannel that the user belongs to.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelMessageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelMessageRequest:
    out: DeleteChannelMessageRequest = {}  # type: ignore[typeddict-item]
    return out
