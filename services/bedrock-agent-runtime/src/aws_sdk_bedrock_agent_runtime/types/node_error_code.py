"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

NodeErrorCode: TypeAlias = Literal[
    "VALIDATION",
    "DEPENDENCY_FAILED",
    "BAD_GATEWAY",
    "INTERNAL_SERVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALIDATION",
        "DEPENDENCY_FAILED",
        "BAD_GATEWAY",
        "INTERNAL_SERVER",
    )
)


def serialize_json(value: NodeErrorCode) -> str:
    return value


def deserialize_json(data: str) -> NodeErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeErrorCode value: {data!r}")
    return cast(NodeErrorCode, data)
