"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationJobType``."""

from typing import Literal, TypeAlias, cast

EvaluationJobType: TypeAlias = Literal[
    "Human",
    "Automated",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationJobType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationJobType:
    return cast(EvaluationJobType, data)
