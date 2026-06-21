"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestionType``."""

from typing import Literal, TypeAlias, cast

EvaluationFormQuestionType: TypeAlias = Literal[
    "TEXT",
    "SINGLESELECT",
    "NUMERIC",
    "MULTISELECT",
    "DATETIME",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormQuestionType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormQuestionType:
    return cast(EvaluationFormQuestionType, data)
