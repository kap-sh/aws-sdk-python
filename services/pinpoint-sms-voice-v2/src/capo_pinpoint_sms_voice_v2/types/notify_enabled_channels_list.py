"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyEnabledChannelsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.number_capability

NotifyEnabledChannelsList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.number_capability.NumberCapability"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyEnabledChannelsList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NotifyEnabledChannelsList:
    return list(data)
