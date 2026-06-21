"""Generated from Smithy shape ``com.amazonaws.backup#ScanJobState``."""

from typing import Literal, TypeAlias, cast

ScanJobState: TypeAlias = Literal[
    "COMPLETED",
    "COMPLETED_WITH_ISSUES",
    "FAILED",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanJobState) -> str:
    return value


def deserialize_json(data: str) -> ScanJobState:
    return cast(ScanJobState, data)
