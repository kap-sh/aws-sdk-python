"""Generated from Smithy shape ``com.amazonaws.datasync#AgentStatus``."""

from typing import Literal, TypeAlias, cast

AgentStatus: TypeAlias = Literal[
    "ONLINE",
    "OFFLINE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentStatus:
    return cast(AgentStatus, data)
