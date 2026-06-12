"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetChannelMessageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.message_id
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id


class GetChannelMessageRequest(TypedDict):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    message_id: "aws_sdk_chime_sdk_messaging.types.message_id.MessageId"
    """<p>The ID of the message.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting messages in a SubChannel that the user belongs to.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelMessageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChannelMessageRequest:
    out: GetChannelMessageRequest = {}  # type: ignore[typeddict-item]
    return out
