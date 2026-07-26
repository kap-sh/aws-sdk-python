"""Generated from Smithy shape ``com.amazonaws.ecs#AgentUpdateStatus``."""

from typing import Literal, TypeAlias, cast

AgentUpdateStatus: TypeAlias = Literal[
    "PENDING",
    "STAGING",
    "STAGED",
    "UPDATING",
    "UPDATED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentUpdateStatus:
    return cast(AgentUpdateStatus, data)
