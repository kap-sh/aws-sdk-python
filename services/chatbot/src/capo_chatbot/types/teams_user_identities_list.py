"""Generated from Smithy shape ``com.amazonaws.chatbot#TeamsUserIdentitiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chatbot.types.teams_user_identity

TeamsUserIdentitiesList: TypeAlias = list[
    "capo_chatbot.types.teams_user_identity.TeamsUserIdentity"
]


# --- restJson1 ser/de ---
def serialize_json(value: TeamsUserIdentitiesList) -> list:
    import capo_chatbot.types.teams_user_identity

    out: list = []
    for item in value:
        out.append(capo_chatbot.types.teams_user_identity.serialize_json(item))
    return out


def deserialize_json(data: list) -> TeamsUserIdentitiesList:
    import capo_chatbot.types.teams_user_identity

    out: TeamsUserIdentitiesList = []
    for item in data:
        out.append(capo_chatbot.types.teams_user_identity.deserialize_json(item))
    return out
