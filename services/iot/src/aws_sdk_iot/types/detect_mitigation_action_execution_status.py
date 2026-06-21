"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionExecutionStatus``."""

from typing import Literal, TypeAlias, cast

DetectMitigationActionExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> DetectMitigationActionExecutionStatus:
    return cast(DetectMitigationActionExecutionStatus, data)
