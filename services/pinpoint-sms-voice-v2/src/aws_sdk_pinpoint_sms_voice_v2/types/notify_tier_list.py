"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyTierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier

NotifyTierList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier.NotifyConfigurationTier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyTierList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NotifyTierList:
    return list(data)
