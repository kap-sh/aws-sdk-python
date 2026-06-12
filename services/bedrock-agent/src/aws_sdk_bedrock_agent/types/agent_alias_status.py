"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

AgentAliasStatus: TypeAlias = Literal[
    "CREATING",
    "PREPARED",
    "FAILED",
    "UPDATING",
    "DELETING",
    "DISSOCIATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "PREPARED",
        "FAILED",
        "UPDATING",
        "DELETING",
        "DISSOCIATED",
    )
)


def serialize_json(value: AgentAliasStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentAliasStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentAliasStatus value: {data!r}")
    return cast(AgentAliasStatus, data)
