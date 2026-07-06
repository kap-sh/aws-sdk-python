"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#VoiceMessageContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.call_instructions_message_type
    import aws_sdk_pinpoint_sms_voice.types.plain_text_message_type
    import aws_sdk_pinpoint_sms_voice.types.ssml_message_type


class VoiceMessageContent(TypedDict, closed=True):
    call_instructions_message: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.call_instructions_message_type.CallInstructionsMessageType"
    ]
    plain_text_message: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.plain_text_message_type.PlainTextMessageType"
    ]
    ssml_message: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.ssml_message_type.SSMLMessageType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceMessageContent) -> dict:
    out: dict = {}
    if "call_instructions_message" in value:
        import aws_sdk_pinpoint_sms_voice.types.call_instructions_message_type

        out["CallInstructionsMessage"] = (
            aws_sdk_pinpoint_sms_voice.types.call_instructions_message_type.serialize_json(
                value["call_instructions_message"]
            )
        )
    if "plain_text_message" in value:
        import aws_sdk_pinpoint_sms_voice.types.plain_text_message_type

        out["PlainTextMessage"] = (
            aws_sdk_pinpoint_sms_voice.types.plain_text_message_type.serialize_json(
                value["plain_text_message"]
            )
        )
    if "ssml_message" in value:
        import aws_sdk_pinpoint_sms_voice.types.ssml_message_type

        out["SSMLMessage"] = (
            aws_sdk_pinpoint_sms_voice.types.ssml_message_type.serialize_json(
                value["ssml_message"]
            )
        )
    return out


def deserialize_json(data: dict) -> VoiceMessageContent:
    out: VoiceMessageContent = {}  # type: ignore[typeddict-item]
    if "CallInstructionsMessage" in data:
        import aws_sdk_pinpoint_sms_voice.types.call_instructions_message_type

        out["call_instructions_message"] = (
            aws_sdk_pinpoint_sms_voice.types.call_instructions_message_type.deserialize_json(
                data["CallInstructionsMessage"]
            )
        )
    if "PlainTextMessage" in data:
        import aws_sdk_pinpoint_sms_voice.types.plain_text_message_type

        out["plain_text_message"] = (
            aws_sdk_pinpoint_sms_voice.types.plain_text_message_type.deserialize_json(
                data["PlainTextMessage"]
            )
        )
    if "SSMLMessage" in data:
        import aws_sdk_pinpoint_sms_voice.types.ssml_message_type

        out["ssml_message"] = (
            aws_sdk_pinpoint_sms_voice.types.ssml_message_type.deserialize_json(
                data["SSMLMessage"]
            )
        )
    return out
