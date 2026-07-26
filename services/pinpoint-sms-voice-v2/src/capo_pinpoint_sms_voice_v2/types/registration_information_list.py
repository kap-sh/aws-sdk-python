"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_information

RegistrationInformationList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.registration_information.RegistrationInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationInformationList) -> list:
    import capo_pinpoint_sms_voice_v2.types.registration_information

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationInformationList:
    import capo_pinpoint_sms_voice_v2.types.registration_information

    out: RegistrationInformationList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
