"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#SSMLMessageType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.non_empty_string
    import aws_sdk_pinpoint_sms_voice.types.string


class SSMLMessageType(TypedDict, closed=True):
    language_code: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """The language to use when delivering the message. For a complete list of supported languages, see the Amazon Polly Developer Guide."""
    text: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.non_empty_string.NonEmptyString"
    ]
    """The SSML-formatted text to deliver to the recipient."""
    voice_id: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """The name of the voice that you want to use to deliver the message. For a complete list of supported voices, see the Amazon Polly Developer Guide."""


# --- restJson1 ser/de ---
def serialize_json(value: SSMLMessageType) -> dict:
    out: dict = {}
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "text" in value:
        out["Text"] = value["text"]
    if "voice_id" in value:
        out["VoiceId"] = value["voice_id"]
    return out


def deserialize_json(data: dict) -> SSMLMessageType:
    out: SSMLMessageType = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        out["language_code"] = data["LanguageCode"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "VoiceId" in data:
        out["voice_id"] = data["VoiceId"]
    return out
