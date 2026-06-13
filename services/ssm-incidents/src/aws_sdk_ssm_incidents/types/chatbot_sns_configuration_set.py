"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ChatbotSnsConfigurationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.sns_arn

ChatbotSnsConfigurationSet: TypeAlias = list[
    "aws_sdk_ssm_incidents.types.sns_arn.SnsArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatbotSnsConfigurationSet) -> list:
    return list(value)


def deserialize_json(data: list) -> ChatbotSnsConfigurationSet:
    return list(data)
