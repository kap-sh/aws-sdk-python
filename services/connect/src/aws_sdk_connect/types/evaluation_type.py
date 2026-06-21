"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationType``."""

from typing import Literal, TypeAlias, cast

EvaluationType: TypeAlias = Literal[
    "STANDARD",
    "CALIBRATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationType:
    return cast(EvaluationType, data)
