"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyConfigurationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_filter

NotifyConfigurationFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_filter.NotifyConfigurationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyConfigurationFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NotifyConfigurationFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_filter

    out: NotifyConfigurationFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
