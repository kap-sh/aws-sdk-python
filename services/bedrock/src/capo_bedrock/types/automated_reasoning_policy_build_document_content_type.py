"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildDocumentContentType``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningPolicyBuildDocumentContentType: TypeAlias = Literal[
    "pdf",
    "txt",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildDocumentContentType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildDocumentContentType:
    return cast(AutomatedReasoningPolicyBuildDocumentContentType, data)
