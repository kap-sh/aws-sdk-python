"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationDeniedReasonInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_denied_reason_information

RegistrationDeniedReasonInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.registration_denied_reason_information.RegistrationDeniedReasonInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationDeniedReasonInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_denied_reason_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_denied_reason_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationDeniedReasonInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_denied_reason_information

    out: RegistrationDeniedReasonInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_denied_reason_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
