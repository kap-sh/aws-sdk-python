"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeEndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

AgentRuntimeEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "READY",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
        "READY",
        "DELETING",
    )
)


def serialize_json(value: AgentRuntimeEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentRuntimeEndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AgentRuntimeEndpointStatus value: {data!r}"
        )
    return cast(AgentRuntimeEndpointStatus, data)
