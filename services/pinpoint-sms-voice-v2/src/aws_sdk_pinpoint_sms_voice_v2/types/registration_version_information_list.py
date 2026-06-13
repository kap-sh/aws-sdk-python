"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationVersionInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information

RegistrationVersionInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information.RegistrationVersionInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationVersionInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationVersionInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information

    out: RegistrationVersionInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
