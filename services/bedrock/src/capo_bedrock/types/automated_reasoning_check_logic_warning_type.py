"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckLogicWarningType``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningCheckLogicWarningType: TypeAlias = Literal[
    "ALWAYS_TRUE",
    "ALWAYS_FALSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckLogicWarningType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningCheckLogicWarningType:
    return cast(AutomatedReasoningCheckLogicWarningType, data)
