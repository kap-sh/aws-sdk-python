"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

ServiceJobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "PENDING",
    "RUNNABLE",
    "SCHEDULED",
    "STARTING",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "PENDING",
        "RUNNABLE",
        "SCHEDULED",
        "STARTING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_json(value: ServiceJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ServiceJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceJobStatus value: {data!r}")
    return cast(ServiceJobStatus, data)
