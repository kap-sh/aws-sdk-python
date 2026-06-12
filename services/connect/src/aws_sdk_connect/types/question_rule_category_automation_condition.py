"""Generated from Smithy shape ``com.amazonaws.connect#QuestionRuleCategoryAutomationCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

QuestionRuleCategoryAutomationCondition: TypeAlias = Literal[
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


def serialize_json(value: QuestionRuleCategoryAutomationCondition) -> str:
    return value


def deserialize_json(data: str) -> QuestionRuleCategoryAutomationCondition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown QuestionRuleCategoryAutomationCondition value: {data!r}"
        )
    return cast(QuestionRuleCategoryAutomationCondition, data)
