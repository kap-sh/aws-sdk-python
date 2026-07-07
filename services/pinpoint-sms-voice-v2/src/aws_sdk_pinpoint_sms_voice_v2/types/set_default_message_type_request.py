"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SetDefaultMessageTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.message_type


class SetDefaultMessageTypeRequest(TypedDict, closed=True):
    configuration_set_name: "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    """<p>The configuration set to update with a new default message type. This field can be the ConsigurationSetName or ConfigurationSetArn.</p>"""
    message_type: "aws_sdk_pinpoint_sms_voice_v2.types.message_type.MessageType"
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetDefaultMessageTypeRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
    out["MessageType"] = value["message_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetDefaultMessageTypeRequest:
    out: SetDefaultMessageTypeRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        raise DeserializationError(
            "SetDefaultMessageTypeRequest.configuration_set_name required"
        )
    if "MessageType" in data:
        out["message_type"] = data["MessageType"]
    else:
        raise DeserializationError("SetDefaultMessageTypeRequest.message_type required")
    return out
