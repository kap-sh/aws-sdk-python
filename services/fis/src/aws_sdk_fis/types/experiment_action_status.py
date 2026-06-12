"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fis.errors import DeserializationError

ExperimentActionStatus: TypeAlias = Literal[
    "pending",
    "initiating",
    "running",
    "completed",
    "cancelled",
    "stopping",
    "stopped",
    "failed",
    "skipped",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "initiating",
        "running",
        "completed",
        "cancelled",
        "stopping",
        "stopped",
        "failed",
        "skipped",
    )
)


def serialize_json(value: ExperimentActionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExperimentActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExperimentActionStatus value: {data!r}")
    return cast(ExperimentActionStatus, data)
