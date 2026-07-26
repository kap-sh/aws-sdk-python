"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.agent_status_id

AgentStatuses: TypeAlias = list["capo_connect.types.agent_status_id.AgentStatusId"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatuses) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentStatuses:
    return list(data)
