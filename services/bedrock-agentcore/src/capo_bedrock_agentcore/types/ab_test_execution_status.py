"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ABTestExecutionStatus: TypeAlias = Literal[
    "PAUSED",
    "RUNNING",
    "STOPPED",
    "NOT_STARTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ABTestExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ABTestExecutionStatus:
    return cast(ABTestExecutionStatus, data)
