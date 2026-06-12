"""Generated from Smithy shape ``com.amazonaws.connect#AgentIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_id

AgentIds: TypeAlias = list["aws_sdk_connect.types.agent_id.AgentId"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentIds) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentIds:
    return list(data)
