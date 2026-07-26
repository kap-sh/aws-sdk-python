"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#CompletionStatus``."""

from typing import Literal, TypeAlias, cast

"""Allowed target statuses for the CompleteTrajectory operation."""
CompletionStatus: TypeAlias = Literal[
    "ready",
    "failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: CompletionStatus) -> str:
    return value


def deserialize_json(data: str) -> CompletionStatus:
    return cast(CompletionStatus, data)
