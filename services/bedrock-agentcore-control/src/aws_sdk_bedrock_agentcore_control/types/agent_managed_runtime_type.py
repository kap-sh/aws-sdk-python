"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentManagedRuntimeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

AgentManagedRuntimeType: TypeAlias = Literal[
    "PYTHON_3_10",
    "PYTHON_3_11",
    "PYTHON_3_12",
    "PYTHON_3_13",
    "PYTHON_3_14",
    "NODE_22",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PYTHON_3_10",
        "PYTHON_3_11",
        "PYTHON_3_12",
        "PYTHON_3_13",
        "PYTHON_3_14",
        "NODE_22",
    )
)


def serialize_json(value: AgentManagedRuntimeType) -> str:
    return value


def deserialize_json(data: str) -> AgentManagedRuntimeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentManagedRuntimeType value: {data!r}")
    return cast(AgentManagedRuntimeType, data)
