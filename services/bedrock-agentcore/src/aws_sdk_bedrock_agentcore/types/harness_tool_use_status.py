"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolUseStatus``."""

from typing import Literal, TypeAlias, cast

HarnessToolUseStatus: TypeAlias = Literal[
    "success",
    "error",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolUseStatus) -> str:
    return value


def deserialize_json(data: str) -> HarnessToolUseStatus:
    return cast(HarnessToolUseStatus, data)
