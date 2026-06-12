"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationFormQuestionType: TypeAlias = Literal[
    "TEXT",
    "SINGLESELECT",
    "NUMERIC",
    "MULTISELECT",
    "DATETIME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "SINGLESELECT",
        "NUMERIC",
        "MULTISELECT",
        "DATETIME",
    )
)


def serialize_json(value: EvaluationFormQuestionType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormQuestionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationFormQuestionType value: {data!r}"
        )
    return cast(EvaluationFormQuestionType, data)
