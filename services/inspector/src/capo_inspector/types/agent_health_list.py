"""Generated from Smithy shape ``com.amazonaws.inspector#AgentHealthList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.agent_health

AgentHealthList: TypeAlias = list["capo_inspector.types.agent_health.AgentHealth"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentHealthList) -> list:
    import capo_inspector.types.agent_health

    out: list = []
    for item in value:
        out.append(capo_inspector.types.agent_health.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AgentHealthList:
    import capo_inspector.types.agent_health

    out: AgentHealthList = []
    for item in data:
        out.append(capo_inspector.types.agent_health.deserialize_aws_json_1_1(item))
    return out
