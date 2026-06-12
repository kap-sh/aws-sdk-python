"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AgentIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.agent_id

AgentIds: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.agent_id.AgentId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AgentIds:
    return list(data)
