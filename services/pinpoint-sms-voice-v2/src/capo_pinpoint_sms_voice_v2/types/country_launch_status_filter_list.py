"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CountryLaunchStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.country_launch_status_filter

CountryLaunchStatusFilterList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.country_launch_status_filter.CountryLaunchStatusFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountryLaunchStatusFilterList) -> list:
    import capo_pinpoint_sms_voice_v2.types.country_launch_status_filter

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.country_launch_status_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CountryLaunchStatusFilterList:
    import capo_pinpoint_sms_voice_v2.types.country_launch_status_filter

    out: CountryLaunchStatusFilterList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.country_launch_status_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
