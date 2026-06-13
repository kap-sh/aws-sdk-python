"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowControlNodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FlowControlNodeType: TypeAlias = Literal[
    "Iterator",
    "Loop",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Iterator",
        "Loop",
    )
)


def serialize_json(value: FlowControlNodeType) -> str:
    return value


def deserialize_json(data: str) -> FlowControlNodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowControlNodeType value: {data!r}")
    return cast(FlowControlNodeType, data)
