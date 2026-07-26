"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PhoneNumberInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.phone_number_information

PhoneNumberInformationList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.phone_number_information.PhoneNumberInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PhoneNumberInformationList) -> list:
    import capo_pinpoint_sms_voice_v2.types.phone_number_information

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.phone_number_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PhoneNumberInformationList:
    import capo_pinpoint_sms_voice_v2.types.phone_number_information

    out: PhoneNumberInformationList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.phone_number_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
