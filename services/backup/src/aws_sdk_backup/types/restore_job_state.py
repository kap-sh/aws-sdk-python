"""Generated from Smithy shape ``com.amazonaws.backup#RestoreJobState``."""

from typing import Literal, TypeAlias, cast

RestoreJobState: TypeAlias = Literal[
    "CREATED",
    "PENDING",
    "RUNNING",
    "ABORTED",
    "COMPLETED",
    "FAILED",
    "AGGREGATE_ALL",
    "ANY",
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreJobState) -> str:
    return value


def deserialize_json(data: str) -> RestoreJobState:
    return cast(RestoreJobState, data)
