"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConfigurationSetNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn

ConfigurationSetNameList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationSetNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ConfigurationSetNameList:
    return list(data)
