"""Generated from Smithy shape ``com.amazonaws.connect#AiAgents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.ai_agent_info

AiAgents: TypeAlias = list["aws_sdk_connect.types.ai_agent_info.AiAgentInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: AiAgents) -> list:
    import aws_sdk_connect.types.ai_agent_info

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.ai_agent_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AiAgents:
    import aws_sdk_connect.types.ai_agent_info

    out: AiAgents = []
    for item in data:
        out.append(aws_sdk_connect.types.ai_agent_info.deserialize_json(item))
    return out
