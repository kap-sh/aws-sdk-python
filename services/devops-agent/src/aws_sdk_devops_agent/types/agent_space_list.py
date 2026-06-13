"""Generated from Smithy shape ``com.amazonaws.devopsagent#AgentSpaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space

AgentSpaceList: TypeAlias = list["aws_sdk_devops_agent.types.agent_space.AgentSpace"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpaceList) -> list:
    import aws_sdk_devops_agent.types.agent_space

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.agent_space.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentSpaceList:
    import aws_sdk_devops_agent.types.agent_space

    out: AgentSpaceList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.agent_space.deserialize_json(item))
    return out
