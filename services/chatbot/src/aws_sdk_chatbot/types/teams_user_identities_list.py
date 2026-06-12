"""Generated from Smithy shape ``com.amazonaws.chatbot#TeamsUserIdentitiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.teams_user_identity

TeamsUserIdentitiesList: TypeAlias = list[
    "aws_sdk_chatbot.types.teams_user_identity.TeamsUserIdentity"
]


# --- restJson1 ser/de ---
def serialize_json(value: TeamsUserIdentitiesList) -> list:
    import aws_sdk_chatbot.types.teams_user_identity

    out: list = []
    for item in value:
        out.append(aws_sdk_chatbot.types.teams_user_identity.serialize_json(item))
    return out


def deserialize_json(data: list) -> TeamsUserIdentitiesList:
    import aws_sdk_chatbot.types.teams_user_identity

    out: TeamsUserIdentitiesList = []
    for item in data:
        out.append(aws_sdk_chatbot.types.teams_user_identity.deserialize_json(item))
    return out
