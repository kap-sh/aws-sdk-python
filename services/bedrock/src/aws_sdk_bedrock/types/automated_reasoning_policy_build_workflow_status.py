"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowStatus``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningPolicyBuildWorkflowStatus: TypeAlias = Literal[
    "SCHEDULED",
    "CANCEL_REQUESTED",
    "PREPROCESSING",
    "BUILDING",
    "TESTING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildWorkflowStatus:
    return cast(AutomatedReasoningPolicyBuildWorkflowStatus, data)
