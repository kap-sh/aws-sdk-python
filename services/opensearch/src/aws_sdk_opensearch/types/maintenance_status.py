"""Generated from Smithy shape ``com.amazonaws.opensearch#MaintenanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

MaintenanceStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "TIMED_OUT",
    )
)


def serialize_json(value: MaintenanceStatus) -> str:
    return value


def deserialize_json(data: str) -> MaintenanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceStatus value: {data!r}")
    return cast(MaintenanceStatus, data)
