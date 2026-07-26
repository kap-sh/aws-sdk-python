"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ProtectConfigurationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn

ProtectConfigurationIdList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProtectConfigurationIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ProtectConfigurationIdList:
    return list(data)
