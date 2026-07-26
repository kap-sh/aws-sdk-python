"""Generated from Smithy shape ``com.amazonaws.iot#AuditTaskStatus``."""

from typing import Literal, TypeAlias, cast

AuditTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> AuditTaskStatus:
    return cast(AuditTaskStatus, data)
