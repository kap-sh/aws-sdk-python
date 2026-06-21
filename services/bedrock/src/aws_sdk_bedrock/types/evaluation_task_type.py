"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationTaskType``."""

from typing import Literal, TypeAlias, cast

EvaluationTaskType: TypeAlias = Literal[
    "Summarization",
    "Classification",
    "QuestionAndAnswer",
    "Generation",
    "Custom",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationTaskType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationTaskType:
    return cast(EvaluationTaskType, data)
