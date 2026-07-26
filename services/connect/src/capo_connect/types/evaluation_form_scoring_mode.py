"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormScoringMode``."""

from typing import Literal, TypeAlias, cast

EvaluationFormScoringMode: TypeAlias = Literal[
    "QUESTION_ONLY",
    "SECTION_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormScoringMode) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormScoringMode:
    return cast(EvaluationFormScoringMode, data)
