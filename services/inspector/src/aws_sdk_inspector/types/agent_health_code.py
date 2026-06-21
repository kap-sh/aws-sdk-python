"""Generated from Smithy shape ``com.amazonaws.inspector#AgentHealthCode``."""

from typing import Literal, TypeAlias, cast

AgentHealthCode: TypeAlias = Literal[
    "IDLE",
    "RUNNING",
    "SHUTDOWN",
    "UNHEALTHY",
    "THROTTLED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentHealthCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentHealthCode:
    return cast(AgentHealthCode, data)
