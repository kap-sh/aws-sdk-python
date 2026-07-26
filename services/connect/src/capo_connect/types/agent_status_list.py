"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.agent_status

AgentStatusList: TypeAlias = list["capo_connect.types.agent_status.AgentStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusList) -> list:
    import capo_connect.types.agent_status

    out: list = []
    for item in value:
        out.append(capo_connect.types.agent_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentStatusList:
    import capo_connect.types.agent_status

    out: AgentStatusList = []
    for item in data:
        out.append(capo_connect.types.agent_status.deserialize_json(item))
    return out
