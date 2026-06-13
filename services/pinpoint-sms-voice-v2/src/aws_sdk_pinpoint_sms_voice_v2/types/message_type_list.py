"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#MessageTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.message_type

MessageTypeList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.message_type.MessageType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> MessageTypeList:
    return list(data)
