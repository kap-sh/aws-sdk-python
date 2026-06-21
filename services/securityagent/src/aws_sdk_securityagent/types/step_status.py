"""Generated from Smithy shape ``com.amazonaws.securityagent#StepStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Pentest job step status.</p>"""
StepStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: StepStatus) -> str:
    return value


def deserialize_json(data: str) -> StepStatus:
    return cast(StepStatus, data)
