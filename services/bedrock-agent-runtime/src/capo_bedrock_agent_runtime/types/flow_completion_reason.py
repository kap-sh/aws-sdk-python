"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowCompletionReason``."""

from typing import Literal, TypeAlias, cast

FlowCompletionReason: TypeAlias = Literal[
    "SUCCESS",
    "INPUT_REQUIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowCompletionReason) -> str:
    return value


def deserialize_json(data: str) -> FlowCompletionReason:
    return cast(FlowCompletionReason, data)
