"""Generated from Smithy shape ``com.amazonaws.connect#MultiSelectQuestionRuleCategoryAutomationCondition``."""

from typing import Literal, TypeAlias, cast

MultiSelectQuestionRuleCategoryAutomationCondition: TypeAlias = Literal[
    "PRESENT",
    "NOT_PRESENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiSelectQuestionRuleCategoryAutomationCondition) -> str:
    return value


def deserialize_json(data: str) -> MultiSelectQuestionRuleCategoryAutomationCondition:
    return cast(MultiSelectQuestionRuleCategoryAutomationCondition, data)
