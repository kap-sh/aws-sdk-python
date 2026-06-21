"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobState``."""

from typing import Literal, TypeAlias, cast

CopyJobState: TypeAlias = Literal[
    "CREATED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "PARTIAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobState) -> str:
    return value


def deserialize_json(data: str) -> CopyJobState:
    return cast(CopyJobState, data)
