"""Generated from Smithy shape ``com.amazonaws.mpa#SessionExecutionStatus``."""

from typing import Literal, TypeAlias, cast

SessionExecutionStatus: TypeAlias = Literal[
    "EXECUTED",
    "FAILED",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionExecutionStatus:
    return cast(SessionExecutionStatus, data)
