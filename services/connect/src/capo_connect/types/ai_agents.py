"""Generated from Smithy shape ``com.amazonaws.connect#AiAgents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.ai_agent_info

AiAgents: TypeAlias = list["capo_connect.types.ai_agent_info.AiAgentInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: AiAgents) -> list:
    import capo_connect.types.ai_agent_info

    out: list = []
    for item in value:
        out.append(capo_connect.types.ai_agent_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AiAgents:
    import capo_connect.types.ai_agent_info

    out: AiAgents = []
    for item in data:
        out.append(capo_connect.types.ai_agent_info.deserialize_json(item))
    return out
