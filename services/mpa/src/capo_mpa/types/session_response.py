"""Generated from Smithy shape ``com.amazonaws.mpa#SessionResponse``."""

from typing import Literal, TypeAlias, cast

SessionResponse: TypeAlias = Literal[
    "APPROVED",
    "REJECTED",
    "NO_RESPONSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionResponse) -> str:
    return value


def deserialize_json(data: str) -> SessionResponse:
    return cast(SessionResponse, data)
