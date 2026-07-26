"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildDocumentBlob``."""

import base64
from typing import TypeAlias

AutomatedReasoningPolicyBuildDocumentBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildDocumentBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildDocumentBlob:
    return base64.b64decode(data)
