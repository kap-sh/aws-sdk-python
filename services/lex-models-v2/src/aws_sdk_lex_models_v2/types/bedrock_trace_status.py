"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BedrockTraceStatus``."""

from typing import Literal, TypeAlias, cast

BedrockTraceStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BedrockTraceStatus) -> str:
    return value


def deserialize_json(data: str) -> BedrockTraceStatus:
    return cast(BedrockTraceStatus, data)
