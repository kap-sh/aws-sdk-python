"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssistantMessage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.assistant_message_block

AssistantMessage: TypeAlias = list[
    "capo_devops_agent.types.assistant_message_block.AssistantMessageBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssistantMessage) -> list:
    import capo_devops_agent.types.assistant_message_block

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.assistant_message_block.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssistantMessage:
    import capo_devops_agent.types.assistant_message_block

    out: AssistantMessage = []
    for item in data:
        out.append(
            capo_devops_agent.types.assistant_message_block.deserialize_json(item)
        )
    return out
