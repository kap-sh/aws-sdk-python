"""Generated from Smithy shape ``com.amazonaws.securityhub#WorkflowStatus``."""

from typing import Literal, TypeAlias, cast

WorkflowStatus: TypeAlias = Literal[
    "NEW",
    "NOTIFIED",
    "RESOLVED",
    "SUPPRESSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStatus:
    return cast(WorkflowStatus, data)
