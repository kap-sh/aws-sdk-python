"""Generated from Smithy shape ``com.amazonaws.inspector#AgentHealth``."""

from typing import Literal, TypeAlias, cast

AgentHealth: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentHealth) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentHealth:
    return cast(AgentHealth, data)
