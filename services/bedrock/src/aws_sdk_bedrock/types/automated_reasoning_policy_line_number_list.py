"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyLineNumberList``."""

from typing import TypeAlias

AutomatedReasoningPolicyLineNumberList: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyLineNumberList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutomatedReasoningPolicyLineNumberList:
    return list(data)
