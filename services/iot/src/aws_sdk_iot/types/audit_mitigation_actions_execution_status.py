"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionsExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuditMitigationActionsExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "CANCELED",
    "SKIPPED",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "CANCELED",
        "SKIPPED",
        "PENDING",
    )
)


def serialize_json(value: AuditMitigationActionsExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> AuditMitigationActionsExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AuditMitigationActionsExecutionStatus value: {data!r}"
        )
    return cast(AuditMitigationActionsExecutionStatus, data)
