"""Generated from Smithy shape ``com.amazonaws.inspector#AgentIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_id

AgentIdList: TypeAlias = list["aws_sdk_inspector.types.agent_id.AgentId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AgentIdList:
    return list(data)
