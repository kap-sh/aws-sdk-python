"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainingInputMode``."""

from typing import Literal, TypeAlias, cast

TrainingInputMode: TypeAlias = Literal[
    "File",
    "FastFile",
    "Pipe",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainingInputMode) -> str:
    return value


def deserialize_json(data: str) -> TrainingInputMode:
    return cast(TrainingInputMode, data)
