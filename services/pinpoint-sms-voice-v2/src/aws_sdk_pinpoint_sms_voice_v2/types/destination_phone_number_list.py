"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DestinationPhoneNumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number

DestinationPhoneNumberList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DestinationPhoneNumberList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> DestinationPhoneNumberList:
    return list(data)
