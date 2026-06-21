"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorType``."""

from typing import Literal, TypeAlias, cast

EvaluatorType: TypeAlias = Literal[
    "Builtin",
    "Custom",
    "CustomCode",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorType) -> str:
    return value


def deserialize_json(data: str) -> EvaluatorType:
    return cast(EvaluatorType, data)
