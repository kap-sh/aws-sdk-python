"""Generated from Smithy shape ``com.amazonaws.deadline#StepParameterType``."""

from typing import Literal, TypeAlias, cast

StepParameterType: TypeAlias = Literal[
    "INT",
    "FLOAT",
    "STRING",
    "PATH",
    "CHUNK_INT",
]


# --- restJson1 ser/de ---
def serialize_json(value: StepParameterType) -> str:
    return value


def deserialize_json(data: str) -> StepParameterType:
    return cast(StepParameterType, data)
