"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyCountryInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_country_information

NotifyCountryInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.notify_country_information.NotifyCountryInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyCountryInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_country_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.notify_country_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NotifyCountryInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_country_information

    out: NotifyCountryInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.notify_country_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
