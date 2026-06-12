"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationQuestionAnswerAnalysisType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationQuestionAnswerAnalysisType: TypeAlias = Literal[
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


def serialize_json(value: EvaluationQuestionAnswerAnalysisType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationQuestionAnswerAnalysisType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationQuestionAnswerAnalysisType value: {data!r}"
        )
    return cast(EvaluationQuestionAnswerAnalysisType, data)
