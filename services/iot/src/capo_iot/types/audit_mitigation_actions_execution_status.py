"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionsExecutionStatus``."""

from typing import Literal, TypeAlias, cast

AuditMitigationActionsExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "CANCELED",
    "SKIPPED",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditMitigationActionsExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> AuditMitigationActionsExecutionStatus:
    return cast(AuditMitigationActionsExecutionStatus, data)
