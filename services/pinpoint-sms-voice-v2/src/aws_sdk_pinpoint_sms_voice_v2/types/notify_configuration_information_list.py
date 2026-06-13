"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyConfigurationInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_information

NotifyConfigurationInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_information.NotifyConfigurationInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyConfigurationInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NotifyConfigurationInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_information

    out: NotifyConfigurationInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
