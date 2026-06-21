"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningLogicWarningType``."""

from typing import Literal, TypeAlias, cast

GuardrailAutomatedReasoningLogicWarningType: TypeAlias = Literal[
    "ALWAYS_FALSE",
    "ALWAYS_TRUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningLogicWarningType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailAutomatedReasoningLogicWarningType:
    return cast(GuardrailAutomatedReasoningLogicWarningType, data)
