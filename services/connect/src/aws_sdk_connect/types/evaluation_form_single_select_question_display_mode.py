"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionDisplayMode``."""

from typing import Literal, TypeAlias, cast

EvaluationFormSingleSelectQuestionDisplayMode: TypeAlias = Literal[
    "DROPDOWN",
    "RADIO",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSingleSelectQuestionDisplayMode) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormSingleSelectQuestionDisplayMode:
    return cast(EvaluationFormSingleSelectQuestionDisplayMode, data)
