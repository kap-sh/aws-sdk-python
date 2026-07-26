"""Generated from Smithy shape ``com.amazonaws.mpa#SessionStatus``."""

from typing import Literal, TypeAlias, cast

SessionStatus: TypeAlias = Literal[
    "PENDING",
    "CANCELLED",
    "APPROVED",
    "FAILED",
    "CREATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionStatus:
    return cast(SessionStatus, data)
