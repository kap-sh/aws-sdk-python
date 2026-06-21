"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionStatus``."""

from typing import Literal, TypeAlias, cast

SessionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    return cast(SessionStatus, data)
