"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

Status: TypeAlias = Literal[
    "NOT_STARTED",
    "STARTING",
    "FAILED_START",
    "RUNNING",
    "STOPPING",
    "FAILED_STOP",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "STARTING",
        "FAILED_START",
        "RUNNING",
        "STOPPING",
        "FAILED_STOP",
        "STOPPED",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
