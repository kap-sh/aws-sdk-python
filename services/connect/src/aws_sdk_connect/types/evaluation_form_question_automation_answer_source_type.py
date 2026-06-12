"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestionAutomationAnswerSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormQuestionAutomationAnswerSourceType: TypeAlias = Literal[
    "CONTACT_LENS_DATA",
    "GEN_AI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTACT_LENS_DATA",
        "GEN_AI",
    )
)


def serialize_json(value: EvaluationFormQuestionAutomationAnswerSourceType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormQuestionAutomationAnswerSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormQuestionAutomationAnswerSourceType value: {data!r}"
        )
    return cast(EvaluationFormQuestionAutomationAnswerSourceType, data)
