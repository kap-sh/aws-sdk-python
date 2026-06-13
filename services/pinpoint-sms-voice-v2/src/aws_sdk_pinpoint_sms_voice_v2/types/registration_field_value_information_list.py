"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationFieldValueInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information

RegistrationFieldValueInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information.RegistrationFieldValueInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationFieldValueInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationFieldValueInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information

    out: RegistrationFieldValueInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
