"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormScoringStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationFormScoringStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormScoringStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormScoringStatus:
    return cast(EvaluationFormScoringStatus, data)
