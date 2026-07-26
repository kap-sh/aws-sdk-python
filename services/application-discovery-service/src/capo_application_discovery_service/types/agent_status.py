"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AgentStatus``."""

from typing import Literal, TypeAlias, cast

AgentStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "RUNNING",
    "UNKNOWN",
    "BLACKLISTED",
    "SHUTDOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentStatus:
    return cast(AgentStatus, data)
