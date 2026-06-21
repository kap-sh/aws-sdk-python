"""Generated from Smithy shape ``com.amazonaws.backup#ScanState``."""

from typing import Literal, TypeAlias, cast

ScanState: TypeAlias = Literal[
    "CANCELED",
    "COMPLETED",
    "COMPLETED_WITH_ISSUES",
    "CREATED",
    "FAILED",
    "RUNNING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanState) -> str:
    return value


def deserialize_json(data: str) -> ScanState:
    return cast(ScanState, data)
