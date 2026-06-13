"""Generated from Smithy shape ``com.amazonaws.devopsagent#PendingMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.pending_message

PendingMessages: TypeAlias = list[
    "aws_sdk_devops_agent.types.pending_message.PendingMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: PendingMessages) -> list:
    import aws_sdk_devops_agent.types.pending_message

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.pending_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> PendingMessages:
    import aws_sdk_devops_agent.types.pending_message

    out: PendingMessages = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.pending_message.deserialize_json(item))
    return out
