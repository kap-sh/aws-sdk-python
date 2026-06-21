"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildMessageType``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningPolicyBuildMessageType: TypeAlias = Literal[
    "INFO",
    "WARNING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildMessageType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildMessageType:
    return cast(AutomatedReasoningPolicyBuildMessageType, data)
