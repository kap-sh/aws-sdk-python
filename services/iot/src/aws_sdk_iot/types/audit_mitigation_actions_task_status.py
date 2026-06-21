"""Generated from Smithy shape ``com.amazonaws.iot#AuditMitigationActionsTaskStatus``."""

from typing import Literal, TypeAlias, cast

AuditMitigationActionsTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditMitigationActionsTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> AuditMitigationActionsTaskStatus:
    return cast(AuditMitigationActionsTaskStatus, data)
