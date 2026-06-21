"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormVersionStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationFormVersionStatus: TypeAlias = Literal[
    "DRAFT",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormVersionStatus:
    return cast(EvaluationFormVersionStatus, data)
