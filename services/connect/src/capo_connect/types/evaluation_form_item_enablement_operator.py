"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementOperator``."""

from typing import Literal, TypeAlias, cast

EvaluationFormItemEnablementOperator: TypeAlias = Literal[
    "OR",
    "AND",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementOperator) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemEnablementOperator:
    return cast(EvaluationFormItemEnablementOperator, data)
