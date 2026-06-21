"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestRunStatus``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningPolicyTestRunStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "SCHEDULED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTestRunStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyTestRunStatus:
    return cast(AutomatedReasoningPolicyTestRunStatus, data)
