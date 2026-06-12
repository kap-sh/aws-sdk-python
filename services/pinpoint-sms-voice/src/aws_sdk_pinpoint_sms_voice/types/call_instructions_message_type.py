"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#CallInstructionsMessageType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.non_empty_string


class CallInstructionsMessageType(TypedDict):
    text: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.non_empty_string.NonEmptyString"
    ]
    """The language to use when delivering the message. For a complete list of supported languages, see the Amazon Polly Developer Guide."""


# --- restJson1 ser/de ---
def serialize_json(value: CallInstructionsMessageType) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    return out


def deserialize_json(data: dict) -> CallInstructionsMessageType:
    out: CallInstructionsMessageType = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    return out
