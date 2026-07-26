"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CountryLaunchStatusInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.country_launch_status_information

CountryLaunchStatusInformationList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.country_launch_status_information.CountryLaunchStatusInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountryLaunchStatusInformationList) -> list:
    import capo_pinpoint_sms_voice_v2.types.country_launch_status_information

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.country_launch_status_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CountryLaunchStatusInformationList:
    import capo_pinpoint_sms_voice_v2.types.country_launch_status_information

    out: CountryLaunchStatusInformationList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.country_launch_status_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
