"""Generated from Smithy shape ``com.amazonaws.connect#SingleSelectQuestionRuleCategoryAutomationCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SingleSelectQuestionRuleCategoryAutomationCondition: TypeAlias = Literal[
    "PRESENT",
    "NOT_PRESENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRESENT",
        "NOT_PRESENT",
    )
)


def serialize_json(value: SingleSelectQuestionRuleCategoryAutomationCondition) -> str:
    return value


def deserialize_json(data: str) -> SingleSelectQuestionRuleCategoryAutomationCondition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SingleSelectQuestionRuleCategoryAutomationCondition value: {data!r}"
        )
    return cast(SingleSelectQuestionRuleCategoryAutomationCondition, data)
