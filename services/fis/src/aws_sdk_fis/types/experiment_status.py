"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fis.errors import DeserializationError

ExperimentStatus: TypeAlias = Literal[
    "pending",
    "initiating",
    "running",
    "completed",
    "stopping",
    "stopped",
    "failed",
    "cancelled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "initiating",
        "running",
        "completed",
        "stopping",
        "stopped",
        "failed",
        "cancelled",
    )
)


def serialize_json(value: ExperimentStatus) -> str:
    return value


def deserialize_json(data: str) -> ExperimentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExperimentStatus value: {data!r}")
    return cast(ExperimentStatus, data)
