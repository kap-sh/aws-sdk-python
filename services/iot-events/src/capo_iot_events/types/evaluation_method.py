"""Generated from Smithy shape ``com.amazonaws.iotevents#EvaluationMethod``."""

from typing import Literal, TypeAlias, cast

EvaluationMethod: TypeAlias = Literal[
    "BATCH",
    "SERIAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationMethod) -> str:
    return value


def deserialize_json(data: str) -> EvaluationMethod:
    return cast(EvaluationMethod, data)
