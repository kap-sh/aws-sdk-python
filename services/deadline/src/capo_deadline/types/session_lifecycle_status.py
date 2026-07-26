"""Generated from Smithy shape ``com.amazonaws.deadline#SessionLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

SessionLifecycleStatus: TypeAlias = Literal[
    "STARTED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCEEDED",
    "UPDATE_FAILED",
    "ENDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> SessionLifecycleStatus:
    return cast(SessionLifecycleStatus, data)
