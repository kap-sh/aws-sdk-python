"""Generated from Smithy shape ``com.amazonaws.connect#QuestionRuleCategoryAutomationCondition``."""

from typing import Literal, TypeAlias, cast

QuestionRuleCategoryAutomationCondition: TypeAlias = Literal[
    "PRESENT",
    "NOT_PRESENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuestionRuleCategoryAutomationCondition) -> str:
    return value


def deserialize_json(data: str) -> QuestionRuleCategoryAutomationCondition:
    return cast(QuestionRuleCategoryAutomationCondition, data)
