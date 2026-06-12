"""Generated from Smithy shape ``com.amazonaws.chatbot#TeamChannelConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.teams_channel_configuration

TeamChannelConfigurationsList: TypeAlias = list[
    "aws_sdk_chatbot.types.teams_channel_configuration.TeamsChannelConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TeamChannelConfigurationsList) -> list:
    import aws_sdk_chatbot.types.teams_channel_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chatbot.types.teams_channel_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TeamChannelConfigurationsList:
    import aws_sdk_chatbot.types.teams_channel_configuration

    out: TeamChannelConfigurationsList = []
    for item in data:
        out.append(
            aws_sdk_chatbot.types.teams_channel_configuration.deserialize_json(item)
        )
    return out
