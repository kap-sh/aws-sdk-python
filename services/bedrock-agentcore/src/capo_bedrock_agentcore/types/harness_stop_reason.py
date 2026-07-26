"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessStopReason``."""

from typing import Literal, TypeAlias, cast

HarnessStopReason: TypeAlias = Literal[
    "end_turn",
    "tool_use",
    "tool_result",
    "max_tokens",
    "stop_sequence",
    "content_filtered",
    "malformed_model_output",
    "malformed_tool_use",
    "interrupted",
    "partial_turn",
    "model_context_window_exceeded",
    "max_iterations_exceeded",
    "max_output_tokens_exceeded",
    "timeout_exceeded",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessStopReason) -> str:
    return value


def deserialize_json(data: str) -> HarnessStopReason:
    return cast(HarnessStopReason, data)
