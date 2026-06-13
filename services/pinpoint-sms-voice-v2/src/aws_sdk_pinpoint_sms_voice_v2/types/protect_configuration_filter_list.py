"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ProtectConfigurationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_filter

ProtectConfigurationFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_filter.ProtectConfigurationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProtectConfigurationFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProtectConfigurationFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_filter

    out: ProtectConfigurationFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
