"""Generated from Smithy shape ``com.amazonaws.applicationsignals#EvaluationType``."""

from typing import Literal, TypeAlias, cast

EvaluationType: TypeAlias = Literal[
    "PeriodBased",
    "RequestBased",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationType:
    return cast(EvaluationType, data)
