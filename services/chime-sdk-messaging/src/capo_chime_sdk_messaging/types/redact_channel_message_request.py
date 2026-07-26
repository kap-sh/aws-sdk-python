"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#RedactChannelMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.message_id
    import capo_chime_sdk_messaging.types.sub_channel_id


class RedactChannelMessageRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel containing the messages that you want to redact.</p>"""
    message_id: "capo_chime_sdk_messaging.types.message_id.MessageId"
    """<p>The ID of the message being redacted.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedactChannelMessageRequest) -> dict:
    out: dict = {}
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> RedactChannelMessageRequest:
    out: RedactChannelMessageRequest = {}  # type: ignore[typeddict-item]
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
