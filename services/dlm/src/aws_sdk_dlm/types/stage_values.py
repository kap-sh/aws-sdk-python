"""Generated from Smithy shape ``com.amazonaws.dlm#StageValues``."""

from typing import Literal, TypeAlias, cast

StageValues: TypeAlias = Literal[
    "PRE",
    "POST",
]


# --- restJson1 ser/de ---
def serialize_json(value: StageValues) -> str:
    return value


def deserialize_json(data: str) -> StageValues:
    return cast(StageValues, data)
