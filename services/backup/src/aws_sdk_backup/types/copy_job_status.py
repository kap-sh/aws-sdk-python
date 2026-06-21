"""Generated from Smithy shape ``com.amazonaws.backup#CopyJobStatus``."""

from typing import Literal, TypeAlias, cast

CopyJobStatus: TypeAlias = Literal[
    "CREATED",
    "RUNNING",
    "ABORTING",
    "ABORTED",
    "COMPLETING",
    "COMPLETED",
    "FAILING",
    "FAILED",
    "PARTIAL",
    "AGGREGATE_ALL",
    "ANY",
]


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobStatus) -> str:
    return value


def deserialize_json(data: str) -> CopyJobStatus:
    return cast(CopyJobStatus, data)
