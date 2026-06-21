"""Generated from Smithy shape ``com.amazonaws.connect#SingleSelectQuestionRuleCategoryAutomationCondition``."""

from typing import Literal, TypeAlias, cast

SingleSelectQuestionRuleCategoryAutomationCondition: TypeAlias = Literal[
    "PRESENT",
    "NOT_PRESENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SingleSelectQuestionRuleCategoryAutomationCondition) -> str:
    return value


def deserialize_json(data: str) -> SingleSelectQuestionRuleCategoryAutomationCondition:
    return cast(SingleSelectQuestionRuleCategoryAutomationCondition, data)
