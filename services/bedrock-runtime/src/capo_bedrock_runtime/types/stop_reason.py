"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#StopReason``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: StopReason) -> str:
    return value


def deserialize_json(data: str) -> StopReason:
    return cast(StopReason, data)
