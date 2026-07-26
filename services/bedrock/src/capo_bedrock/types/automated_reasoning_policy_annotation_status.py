"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotationStatus``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningPolicyAnnotationStatus: TypeAlias = Literal[
    "APPLIED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotationStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyAnnotationStatus:
    return cast(AutomatedReasoningPolicyAnnotationStatus, data)
