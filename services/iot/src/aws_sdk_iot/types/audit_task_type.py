"""Generated from Smithy shape ``com.amazonaws.iot#AuditTaskType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuditTaskType: TypeAlias = Literal[
    "ON_DEMAND_AUDIT_TASK",
    "SCHEDULED_AUDIT_TASK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND_AUDIT_TASK",
        "SCHEDULED_AUDIT_TASK",
    )
)


def serialize_json(value: AuditTaskType) -> str:
    return value


def deserialize_json(data: str) -> AuditTaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditTaskType value: {data!r}")
    return cast(AuditTaskType, data)
