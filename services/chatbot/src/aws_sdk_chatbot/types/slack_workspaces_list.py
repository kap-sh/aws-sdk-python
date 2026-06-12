"""Generated from Smithy shape ``com.amazonaws.chatbot#SlackWorkspacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.slack_workspace

SlackWorkspacesList: TypeAlias = list[
    "aws_sdk_chatbot.types.slack_workspace.SlackWorkspace"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlackWorkspacesList) -> list:
    import aws_sdk_chatbot.types.slack_workspace

    out: list = []
    for item in value:
        out.append(aws_sdk_chatbot.types.slack_workspace.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlackWorkspacesList:
    import aws_sdk_chatbot.types.slack_workspace

    out: SlackWorkspacesList = []
    for item in data:
        out.append(aws_sdk_chatbot.types.slack_workspace.deserialize_json(item))
    return out
