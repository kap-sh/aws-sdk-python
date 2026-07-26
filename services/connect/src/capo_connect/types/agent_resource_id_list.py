"""Generated from Smithy shape ``com.amazonaws.connect#AgentResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.agent_resource_id

AgentResourceIdList: TypeAlias = list[
    "capo_connect.types.agent_resource_id.AgentResourceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentResourceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentResourceIdList:
    return list(data)
