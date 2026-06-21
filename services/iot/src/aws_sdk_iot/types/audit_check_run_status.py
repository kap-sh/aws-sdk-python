"""Generated from Smithy shape ``com.amazonaws.iot#AuditCheckRunStatus``."""

from typing import Literal, TypeAlias, cast

AuditCheckRunStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "WAITING_FOR_DATA_COLLECTION",
    "CANCELED",
    "COMPLETED_COMPLIANT",
    "COMPLETED_NON_COMPLIANT",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditCheckRunStatus) -> str:
    return value


def deserialize_json(data: str) -> AuditCheckRunStatus:
    return cast(AuditCheckRunStatus, data)
