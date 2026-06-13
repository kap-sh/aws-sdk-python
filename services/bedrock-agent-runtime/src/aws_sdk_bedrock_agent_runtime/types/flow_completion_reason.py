"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowCompletionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FlowCompletionReason: TypeAlias = Literal[
    "SUCCESS",
    "INPUT_REQUIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "INPUT_REQUIRED",
    )
)


def serialize_json(value: FlowCompletionReason) -> str:
    return value


def deserialize_json(data: str) -> FlowCompletionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowCompletionReason value: {data!r}")
    return cast(FlowCompletionReason, data)
