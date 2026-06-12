"""Generated from Smithy shape ``com.amazonaws.chatbot#SlackUserIdentitiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.slack_user_identity

SlackUserIdentitiesList: TypeAlias = list[
    "aws_sdk_chatbot.types.slack_user_identity.SlackUserIdentity"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlackUserIdentitiesList) -> list:
    import aws_sdk_chatbot.types.slack_user_identity

    out: list = []
    for item in value:
        out.append(aws_sdk_chatbot.types.slack_user_identity.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlackUserIdentitiesList:
    import aws_sdk_chatbot.types.slack_user_identity

    out: SlackUserIdentitiesList = []
    for item in data:
        out.append(aws_sdk_chatbot.types.slack_user_identity.deserialize_json(item))
    return out
