"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyConfigurationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn

NotifyConfigurationIdList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.notify_configuration_id_or_arn.NotifyConfigurationIdOrArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyConfigurationIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NotifyConfigurationIdList:
    return list(data)
