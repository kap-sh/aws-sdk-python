"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionDisplayMode``."""

from typing import Literal, TypeAlias, cast

EvaluationFormMultiSelectQuestionDisplayMode: TypeAlias = Literal[
    "DROPDOWN",
    "CHECKBOX",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMultiSelectQuestionDisplayMode) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormMultiSelectQuestionDisplayMode:
    return cast(EvaluationFormMultiSelectQuestionDisplayMode, data)
