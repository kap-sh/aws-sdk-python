"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#SendVoiceMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.non_empty_string
    import aws_sdk_pinpoint_sms_voice.types.string
    import aws_sdk_pinpoint_sms_voice.types.voice_message_content
    import aws_sdk_pinpoint_sms_voice.types.word_characters_with_delimiters


class SendVoiceMessageRequest(TypedDict, closed=True):
    caller_id: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """The phone number that appears on recipients' devices when they receive the message."""
    configuration_set_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.word_characters_with_delimiters.WordCharactersWithDelimiters"
    ]
    """The name of the configuration set that you want to use to send the message."""
    content: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.voice_message_content.VoiceMessageContent"
    ]
    destination_phone_number: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.non_empty_string.NonEmptyString"
    ]
    """The phone number that you want to send the voice message to."""
    origination_phone_number: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.non_empty_string.NonEmptyString"
    ]
    """The phone number that Amazon Pinpoint should use to send the voice message. This isn't necessarily the phone number that appears on recipients' devices when they receive the message, because you can specify a CallerId parameter in the request."""


# --- restJson1 ser/de ---
def serialize_json(value: SendVoiceMessageRequest) -> dict:
    out: dict = {}
    if "caller_id" in value:
        out["CallerId"] = value["caller_id"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "content" in value:
        import aws_sdk_pinpoint_sms_voice.types.voice_message_content

        out["Content"] = (
            aws_sdk_pinpoint_sms_voice.types.voice_message_content.serialize_json(
                value["content"]
            )
        )
    if "destination_phone_number" in value:
        out["DestinationPhoneNumber"] = value["destination_phone_number"]
    if "origination_phone_number" in value:
        out["OriginationPhoneNumber"] = value["origination_phone_number"]
    return out


def deserialize_json(data: dict) -> SendVoiceMessageRequest:
    out: SendVoiceMessageRequest = {}  # type: ignore[typeddict-item]
    if "CallerId" in data:
        out["caller_id"] = data["CallerId"]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if "Content" in data:
        import aws_sdk_pinpoint_sms_voice.types.voice_message_content

        out["content"] = (
            aws_sdk_pinpoint_sms_voice.types.voice_message_content.deserialize_json(
                data["Content"]
            )
        )
    if "DestinationPhoneNumber" in data:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    if "OriginationPhoneNumber" in data:
        out["origination_phone_number"] = data["OriginationPhoneNumber"]
    return out
