"""Generated from Smithy shape ``com.amazonaws.backup#RestoreJobState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "PENDING",
        "RUNNING",
        "ABORTED",
        "COMPLETED",
        "FAILED",
        "AGGREGATE_ALL",
        "ANY",
    )
)


def serialize_json(value: RestoreJobState) -> str:
    return value


def deserialize_json(data: str) -> RestoreJobState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RestoreJobState value: {data!r}")
    return cast(RestoreJobState, data)
