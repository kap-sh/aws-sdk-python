"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ProtectConfigurationInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_information

ProtectConfigurationInformationList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.protect_configuration_information.ProtectConfigurationInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProtectConfigurationInformationList) -> list:
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_information

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.protect_configuration_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProtectConfigurationInformationList:
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_information

    out: ProtectConfigurationInformationList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.protect_configuration_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
