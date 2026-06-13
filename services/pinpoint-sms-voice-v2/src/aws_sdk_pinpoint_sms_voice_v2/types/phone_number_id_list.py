"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PhoneNumberIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number_id_or_arn

PhoneNumberIdList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.phone_number_id_or_arn.PhoneNumberIdOrArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PhoneNumberIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PhoneNumberIdList:
    return list(data)
