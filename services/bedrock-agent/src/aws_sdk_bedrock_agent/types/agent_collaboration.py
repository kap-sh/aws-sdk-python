"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentCollaboration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

AgentCollaboration: TypeAlias = Literal[
    "SUPERVISOR",
    "SUPERVISOR_ROUTER",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUPERVISOR",
        "SUPERVISOR_ROUTER",
        "DISABLED",
    )
)


def serialize_json(value: AgentCollaboration) -> str:
    return value


def deserialize_json(data: str) -> AgentCollaboration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentCollaboration value: {data!r}")
    return cast(AgentCollaboration, data)
