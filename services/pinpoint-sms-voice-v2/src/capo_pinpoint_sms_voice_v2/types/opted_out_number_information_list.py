"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#OptedOutNumberInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.opted_out_number_information

OptedOutNumberInformationList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.opted_out_number_information.OptedOutNumberInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptedOutNumberInformationList) -> list:
    import capo_pinpoint_sms_voice_v2.types.opted_out_number_information

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.opted_out_number_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> OptedOutNumberInformationList:
    import capo_pinpoint_sms_voice_v2.types.opted_out_number_information

    out: OptedOutNumberInformationList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.opted_out_number_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
