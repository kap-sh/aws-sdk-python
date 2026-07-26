"""Generated from Smithy shape ``com.amazonaws.aiops#ChatbotNotificationChannel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_aiops.types.chat_configuration_arns
    import capo_aiops.types.sns_topic_arn

ChatbotNotificationChannel: TypeAlias = dict[
    "capo_aiops.types.sns_topic_arn.SNSTopicArn",
    "capo_aiops.types.chat_configuration_arns.ChatConfigurationArns",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ChatbotNotificationChannel) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_aiops.types.chat_configuration_arns

        out[key] = capo_aiops.types.chat_configuration_arns.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ChatbotNotificationChannel:
    out: ChatbotNotificationChannel = {}
    for key, value in data.items():
        import capo_aiops.types.chat_configuration_arns

        out[key] = capo_aiops.types.chat_configuration_arns.deserialize_json(value)
    return out
