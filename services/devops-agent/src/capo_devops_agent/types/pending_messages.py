"""Generated from Smithy shape ``com.amazonaws.devopsagent#PendingMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.pending_message

PendingMessages: TypeAlias = list[
    "capo_devops_agent.types.pending_message.PendingMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: PendingMessages) -> list:
    import capo_devops_agent.types.pending_message

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.pending_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> PendingMessages:
    import capo_devops_agent.types.pending_message

    out: PendingMessages = []
    for item in data:
        out.append(capo_devops_agent.types.pending_message.deserialize_json(item))
    return out
