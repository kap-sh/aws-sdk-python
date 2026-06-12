"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#CompletionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemakerjobruntime.errors import DeserializationError

"""Allowed target statuses for the CompleteTrajectory operation."""
CompletionStatus: TypeAlias = Literal[
    "ready",
    "failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ready",
        "failed",
    )
)


def serialize_json(value: CompletionStatus) -> str:
    return value


def deserialize_json(data: str) -> CompletionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompletionStatus value: {data!r}")
    return cast(CompletionStatus, data)
