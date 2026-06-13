"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationVersionNumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_number

RegistrationVersionNumberList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationVersionNumberList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RegistrationVersionNumberList:
    return list(data)
