"""Generated from Smithy shape ``com.amazonaws.chatbot#SlackUserIdentitiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chatbot.types.slack_user_identity

SlackUserIdentitiesList: TypeAlias = list[
    "capo_chatbot.types.slack_user_identity.SlackUserIdentity"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlackUserIdentitiesList) -> list:
    import capo_chatbot.types.slack_user_identity

    out: list = []
    for item in value:
        out.append(capo_chatbot.types.slack_user_identity.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlackUserIdentitiesList:
    import capo_chatbot.types.slack_user_identity

    out: SlackUserIdentitiesList = []
    for item in data:
        out.append(capo_chatbot.types.slack_user_identity.deserialize_json(item))
    return out
