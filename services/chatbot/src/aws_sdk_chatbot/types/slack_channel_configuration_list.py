"""Generated from Smithy shape ``com.amazonaws.chatbot#SlackChannelConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.slack_channel_configuration

SlackChannelConfigurationList: TypeAlias = list[
    "aws_sdk_chatbot.types.slack_channel_configuration.SlackChannelConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlackChannelConfigurationList) -> list:
    import aws_sdk_chatbot.types.slack_channel_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chatbot.types.slack_channel_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SlackChannelConfigurationList:
    import aws_sdk_chatbot.types.slack_channel_configuration

    out: SlackChannelConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_chatbot.types.slack_channel_configuration.deserialize_json(item)
        )
    return out
