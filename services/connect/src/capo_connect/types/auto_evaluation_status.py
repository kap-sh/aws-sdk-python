"""Generated from Smithy shape ``com.amazonaws.connect#AutoEvaluationStatus``."""

from typing import Literal, TypeAlias, cast

AutoEvaluationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoEvaluationStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoEvaluationStatus:
    return cast(AutoEvaluationStatus, data)
