"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

AgentStatus: TypeAlias = Literal[
    "CREATING",
    "PREPARING",
    "PREPARED",
    "NOT_PREPARED",
    "DELETING",
    "FAILED",
    "VERSIONING",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "PREPARING",
        "PREPARED",
        "NOT_PREPARED",
        "DELETING",
        "FAILED",
        "VERSIONING",
        "UPDATING",
    )
)


def serialize_json(value: AgentStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentStatus value: {data!r}")
    return cast(AgentStatus, data)
