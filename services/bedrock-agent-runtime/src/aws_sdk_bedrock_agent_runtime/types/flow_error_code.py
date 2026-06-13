"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FlowErrorCode: TypeAlias = Literal[
    "VALIDATION",
    "INTERNAL_SERVER",
    "NODE_EXECUTION_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALIDATION",
        "INTERNAL_SERVER",
        "NODE_EXECUTION_FAILED",
    )
)


def serialize_json(value: FlowErrorCode) -> str:
    return value


def deserialize_json(data: str) -> FlowErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowErrorCode value: {data!r}")
    return cast(FlowErrorCode, data)
