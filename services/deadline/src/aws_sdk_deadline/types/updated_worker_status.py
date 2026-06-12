"""Generated from Smithy shape ``com.amazonaws.deadline#UpdatedWorkerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

UpdatedWorkerStatus: TypeAlias = Literal[
    "STARTED",
    "STOPPING",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTED",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_json(value: UpdatedWorkerStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdatedWorkerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdatedWorkerStatus value: {data!r}")
    return cast(UpdatedWorkerStatus, data)
