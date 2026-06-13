"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NumberCapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.number_capability

NumberCapabilityList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.number_capability.NumberCapability"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NumberCapabilityList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NumberCapabilityList:
    return list(data)
