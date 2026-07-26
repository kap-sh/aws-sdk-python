"""Generated from Smithy shape ``com.amazonaws.securityagent#AgentSpaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space

AgentSpaceList: TypeAlias = list["capo_securityagent.types.agent_space.AgentSpace"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpaceList) -> list:
    import capo_securityagent.types.agent_space

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.agent_space.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentSpaceList:
    import capo_securityagent.types.agent_space

    out: AgentSpaceList = []
    for item in data:
        out.append(capo_securityagent.types.agent_space.deserialize_json(item))
    return out
