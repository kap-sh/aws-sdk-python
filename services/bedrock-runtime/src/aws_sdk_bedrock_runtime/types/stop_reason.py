"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#StopReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

StopReason: TypeAlias = Literal[
    "end_turn",
    "tool_use",
    "max_tokens",
    "stop_sequence",
    "guardrail_intervened",
    "content_filtered",
    "malformed_model_output",
    "malformed_tool_use",
    "model_context_window_exceeded",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "end_turn",
        "tool_use",
        "max_tokens",
        "stop_sequence",
        "guardrail_intervened",
        "content_filtered",
        "malformed_model_output",
        "malformed_tool_use",
        "model_context_window_exceeded",
    )
)


def serialize_json(value: StopReason) -> str:
    return value


def deserialize_json(data: str) -> StopReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StopReason value: {data!r}")
    return cast(StopReason, data)
