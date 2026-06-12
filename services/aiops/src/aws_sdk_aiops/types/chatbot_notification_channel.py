"""Generated from Smithy shape ``com.amazonaws.aiops#ChatbotNotificationChannel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_aiops.types.chat_configuration_arns
    import aws_sdk_aiops.types.sns_topic_arn

ChatbotNotificationChannel: TypeAlias = dict[
    "aws_sdk_aiops.types.sns_topic_arn.SNSTopicArn",
    "aws_sdk_aiops.types.chat_configuration_arns.ChatConfigurationArns",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ChatbotNotificationChannel) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_aiops.types.chat_configuration_arns

        out[key] = aws_sdk_aiops.types.chat_configuration_arns.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ChatbotNotificationChannel:
    out: ChatbotNotificationChannel = {}
    for key, value in data.items():
        import aws_sdk_aiops.types.chat_configuration_arns

        out[key] = aws_sdk_aiops.types.chat_configuration_arns.deserialize_json(value)
    return out
