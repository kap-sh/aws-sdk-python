"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConfigurationSetInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information

ConfigurationSetInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information.ConfigurationSetInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationSetInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConfigurationSetInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information

    out: ConfigurationSetInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
