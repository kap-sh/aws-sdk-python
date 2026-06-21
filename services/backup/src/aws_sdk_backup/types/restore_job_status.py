"""Generated from Smithy shape ``com.amazonaws.backup#RestoreJobStatus``."""

from typing import Literal, TypeAlias, cast

RestoreJobStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "COMPLETED",
    "ABORTED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreJobStatus) -> str:
    return value


def deserialize_json(data: str) -> RestoreJobStatus:
    return cast(RestoreJobStatus, data)
