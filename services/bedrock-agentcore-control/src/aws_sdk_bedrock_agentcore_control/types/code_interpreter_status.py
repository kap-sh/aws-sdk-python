"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

CodeInterpreterStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "READY",
    "DELETING",
    "DELETE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "READY",
        "DELETING",
        "DELETE_FAILED",
        "DELETED",
    )
)


def serialize_json(value: CodeInterpreterStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeInterpreterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeInterpreterStatus value: {data!r}")
    return cast(CodeInterpreterStatus, data)
