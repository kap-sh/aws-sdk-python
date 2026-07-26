"""Generated from Smithy shape ``com.amazonaws.devopsagent#ChatExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.chat_execution

ChatExecutionList: TypeAlias = list[
    "capo_devops_agent.types.chat_execution.ChatExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatExecutionList) -> list:
    import capo_devops_agent.types.chat_execution

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.chat_execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChatExecutionList:
    import capo_devops_agent.types.chat_execution

    out: ChatExecutionList = []
    for item in data:
        out.append(capo_devops_agent.types.chat_execution.deserialize_json(item))
    return out
