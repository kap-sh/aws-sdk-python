"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormScoringMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormScoringMode: TypeAlias = Literal[
    "QUESTION_ONLY",
    "SECTION_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUESTION_ONLY",
        "SECTION_ONLY",
    )
)


def serialize_json(value: EvaluationFormScoringMode) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormScoringMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationFormScoringMode value: {data!r}")
    return cast(EvaluationFormScoringMode, data)
