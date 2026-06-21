"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSuggestedAnswerStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationSuggestedAnswerStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSuggestedAnswerStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationSuggestedAnswerStatus:
    return cast(EvaluationSuggestedAnswerStatus, data)
