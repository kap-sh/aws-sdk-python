"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationStatus: TypeAlias = Literal[
    "DRAFT",
    "SUBMITTED",
    "REVIEW_REQUESTED",
    "UNDER_REVIEW",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationStatus:
    return cast(EvaluationStatus, data)
