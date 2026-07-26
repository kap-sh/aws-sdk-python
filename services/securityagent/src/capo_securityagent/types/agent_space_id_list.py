"""Generated from Smithy shape ``com.amazonaws.securityagent#AgentSpaceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id

AgentSpaceIdList: TypeAlias = list[
    "capo_securityagent.types.agent_space_id.AgentSpaceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpaceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentSpaceIdList:
    return list(data)
