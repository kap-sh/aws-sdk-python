"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementAction``."""

from typing import Literal, TypeAlias, cast

EvaluationFormItemEnablementAction: TypeAlias = Literal[
    "DISABLE",
    "ENABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementAction) -> str:
    return value


def deserialize_json(data: str) -> EvaluationFormItemEnablementAction:
    return cast(EvaluationFormItemEnablementAction, data)
