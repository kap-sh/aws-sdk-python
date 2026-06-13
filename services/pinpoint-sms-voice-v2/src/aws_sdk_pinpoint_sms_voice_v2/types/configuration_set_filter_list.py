"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConfigurationSetFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter

ConfigurationSetFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter.ConfigurationSetFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationSetFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConfigurationSetFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter

    out: ConfigurationSetFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
