"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorLevel``."""

from typing import Literal, TypeAlias, cast

EvaluatorLevel: TypeAlias = Literal[
    "TOOL_CALL",
    "TRACE",
    "SESSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorLevel) -> str:
    return value


def deserialize_json(data: str) -> EvaluatorLevel:
    return cast(EvaluatorLevel, data)
