"""Generated from Smithy shape ``com.amazonaws.connect#MultiSelectQuestionRuleCategoryAutomationCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

MultiSelectQuestionRuleCategoryAutomationCondition: TypeAlias = Literal[
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


def serialize_json(value: MultiSelectQuestionRuleCategoryAutomationCondition) -> str:
    return value


def deserialize_json(data: str) -> MultiSelectQuestionRuleCategoryAutomationCondition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MultiSelectQuestionRuleCategoryAutomationCondition value: {data!r}"
        )
    return cast(MultiSelectQuestionRuleCategoryAutomationCondition, data)
