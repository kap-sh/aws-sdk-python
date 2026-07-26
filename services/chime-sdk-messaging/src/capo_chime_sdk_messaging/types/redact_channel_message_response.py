"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#RedactChannelMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.message_id
    import capo_chime_sdk_messaging.types.sub_channel_id


class RedactChannelMessageResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel containing the messages that you want to redact.</p>"""
    message_id: NotRequired["capo_chime_sdk_messaging.types.message_id.MessageId"]
    """<p>The ID of the message being redacted.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the response.</p> <note> <p>Only required when redacting messages in a SubChannel that the user belongs to.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedactChannelMessageResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> RedactChannelMessageResponse:
    out: RedactChannelMessageResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
