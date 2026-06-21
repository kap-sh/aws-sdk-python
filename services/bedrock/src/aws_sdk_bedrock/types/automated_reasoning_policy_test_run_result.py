"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestRunResult``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningPolicyTestRunResult: TypeAlias = Literal[
    "PASSED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTestRunResult) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyTestRunResult:
    return cast(AutomatedReasoningPolicyTestRunResult, data)
