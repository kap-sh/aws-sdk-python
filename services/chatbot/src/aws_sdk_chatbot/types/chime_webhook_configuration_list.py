"""Generated from Smithy shape ``com.amazonaws.chatbot#ChimeWebhookConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.chime_webhook_configuration

ChimeWebhookConfigurationList: TypeAlias = list[
    "aws_sdk_chatbot.types.chime_webhook_configuration.ChimeWebhookConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChimeWebhookConfigurationList) -> list:
    import aws_sdk_chatbot.types.chime_webhook_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chatbot.types.chime_webhook_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChimeWebhookConfigurationList:
    import aws_sdk_chatbot.types.chime_webhook_configuration

    out: ChimeWebhookConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_chatbot.types.chime_webhook_configuration.deserialize_json(item)
        )
    return out
