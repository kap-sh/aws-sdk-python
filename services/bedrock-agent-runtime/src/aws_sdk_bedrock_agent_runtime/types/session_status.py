"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SessionStatus``."""

from typing import Literal, TypeAlias, cast

SessionStatus: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "ENDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    return cast(SessionStatus, data)
