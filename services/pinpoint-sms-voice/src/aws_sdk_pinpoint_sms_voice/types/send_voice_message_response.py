"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#SendVoiceMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.string


class SendVoiceMessageResponse(TypedDict, closed=True):
    message_id: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """A unique identifier for the voice message."""


# --- restJson1 ser/de ---
def serialize_json(value: SendVoiceMessageResponse) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    return out


def deserialize_json(data: dict) -> SendVoiceMessageResponse:
    out: SendVoiceMessageResponse = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    return out
