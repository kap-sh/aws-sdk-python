"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssistantMessage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.assistant_message_block

AssistantMessage: TypeAlias = list[
    "aws_sdk_devops_agent.types.assistant_message_block.AssistantMessageBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssistantMessage) -> list:
    import aws_sdk_devops_agent.types.assistant_message_block

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_agent.types.assistant_message_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssistantMessage:
    import aws_sdk_devops_agent.types.assistant_message_block

    out: AssistantMessage = []
    for item in data:
        out.append(
            aws_sdk_devops_agent.types.assistant_message_block.deserialize_json(item)
        )
    return out
