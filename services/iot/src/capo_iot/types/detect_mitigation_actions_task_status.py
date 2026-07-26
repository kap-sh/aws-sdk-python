"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionsTaskStatus``."""

from typing import Literal, TypeAlias, cast

DetectMitigationActionsTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionsTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> DetectMitigationActionsTaskStatus:
    return cast(DetectMitigationActionsTaskStatus, data)
