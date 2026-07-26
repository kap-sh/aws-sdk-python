"""Generated from Smithy shape ``com.amazonaws.quicksight#AutomationJobStatus``."""

from typing import Literal, TypeAlias, cast

AutomationJobStatus: TypeAlias = Literal[
    "FAILED",
    "RUNNING",
    "SUCCEEDED",
    "QUEUED",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomationJobStatus:
    return cast(AutomationJobStatus, data)
