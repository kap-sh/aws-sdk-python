"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_id_or_arn

RegistrationIdList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RegistrationIdList:
    return list(data)
