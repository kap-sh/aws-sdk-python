"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyUseCaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.notify_configuration_use_case

NotifyUseCaseList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.notify_configuration_use_case.NotifyConfigurationUseCase"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyUseCaseList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NotifyUseCaseList:
    return list(data)
