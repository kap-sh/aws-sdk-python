"""Generated from Smithy shape ``com.amazonaws.iot#AuditCheckRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuditCheckRunStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "WAITING_FOR_DATA_COLLECTION",
    "CANCELED",
    "COMPLETED_COMPLIANT",
    "COMPLETED_NON_COMPLIANT",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "WAITING_FOR_DATA_COLLECTION",
        "CANCELED",
        "COMPLETED_COMPLIANT",
        "COMPLETED_NON_COMPLIANT",
        "FAILED",
    )
)


def serialize_json(value: AuditCheckRunStatus) -> str:
    return value


def deserialize_json(data: str) -> AuditCheckRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditCheckRunStatus value: {data!r}")
    return cast(AuditCheckRunStatus, data)
