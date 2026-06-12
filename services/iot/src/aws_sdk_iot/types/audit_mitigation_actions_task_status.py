"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionsTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuditMitigationActionsTaskStatus: TypeAlias = Literal[
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


def serialize_json(value: AuditMitigationActionsTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> AuditMitigationActionsTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AuditMitigationActionsTaskStatus value: {data!r}"
        )
    return cast(AuditMitigationActionsTaskStatus, data)
