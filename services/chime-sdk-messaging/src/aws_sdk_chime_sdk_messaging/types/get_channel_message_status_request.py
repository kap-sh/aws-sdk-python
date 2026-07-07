"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetChannelMessageStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.message_id
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id


class GetChannelMessageStatusRequest(TypedDict, closed=True):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel</p>"""
    message_id: "aws_sdk_chime_sdk_messaging.types.message_id.MessageId"
    """<p>The ID of the message.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting message status in a SubChannel that the user belongs to.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelMessageStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChannelMessageStatusRequest:
    out: GetChannelMessageStatusRequest = {}  # type: ignore[typeddict-item]
    return out
