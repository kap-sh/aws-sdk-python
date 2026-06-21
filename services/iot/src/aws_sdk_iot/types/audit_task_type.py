"""Generated from Smithy shape ``com.amazonaws.iot#AuditTaskType``."""

from typing import Literal, TypeAlias, cast

AuditTaskType: TypeAlias = Literal[
    "ON_DEMAND_AUDIT_TASK",
    "SCHEDULED_AUDIT_TASK",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditTaskType) -> str:
    return value


def deserialize_json(data: str) -> AuditTaskType:
    return cast(AuditTaskType, data)
