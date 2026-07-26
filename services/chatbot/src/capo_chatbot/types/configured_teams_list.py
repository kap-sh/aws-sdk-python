"""Generated from Smithy shape ``com.amazonaws.chatbot#ConfiguredTeamsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chatbot.types.configured_team

ConfiguredTeamsList: TypeAlias = list[
    "capo_chatbot.types.configured_team.ConfiguredTeam"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTeamsList) -> list:
    import capo_chatbot.types.configured_team

    out: list = []
    for item in value:
        out.append(capo_chatbot.types.configured_team.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfiguredTeamsList:
    import capo_chatbot.types.configured_team

    out: ConfiguredTeamsList = []
    for item in data:
        out.append(capo_chatbot.types.configured_team.deserialize_json(item))
    return out
