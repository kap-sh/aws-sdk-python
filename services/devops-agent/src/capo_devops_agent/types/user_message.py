"""Generated from Smithy shape ``com.amazonaws.devopsagent#UserMessage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.user_message_block

UserMessage: TypeAlias = list[
    "capo_devops_agent.types.user_message_block.UserMessageBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserMessage) -> list:
    import capo_devops_agent.types.user_message_block

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.user_message_block.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserMessage:
    import capo_devops_agent.types.user_message_block

    out: UserMessage = []
    for item in data:
        out.append(capo_devops_agent.types.user_message_block.deserialize_json(item))
    return out
