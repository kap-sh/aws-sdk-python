"""Generated from Smithy shape ``com.amazonaws.iot#AuditTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuditTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "CANCELED",
    )
)


def serialize_json(value: AuditTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> AuditTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditTaskStatus value: {data!r}")
    return cast(AuditTaskStatus, data)
