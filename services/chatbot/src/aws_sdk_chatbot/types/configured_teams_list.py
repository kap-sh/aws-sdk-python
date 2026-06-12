"""Generated from Smithy shape ``com.amazonaws.chatbot#ConfiguredTeamsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.configured_team

ConfiguredTeamsList: TypeAlias = list[
    "aws_sdk_chatbot.types.configured_team.ConfiguredTeam"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTeamsList) -> list:
    import aws_sdk_chatbot.types.configured_team

    out: list = []
    for item in value:
        out.append(aws_sdk_chatbot.types.configured_team.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfiguredTeamsList:
    import aws_sdk_chatbot.types.configured_team

    out: ConfiguredTeamsList = []
    for item in data:
        out.append(aws_sdk_chatbot.types.configured_team.deserialize_json(item))
    return out
