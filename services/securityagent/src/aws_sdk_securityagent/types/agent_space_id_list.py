"""Generated from Smithy shape ``com.amazonaws.securityagent#AgentSpaceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_space_id

AgentSpaceIdList: TypeAlias = list[
    "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpaceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentSpaceIdList:
    return list(data)
