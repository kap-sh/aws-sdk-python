"""Generated from Smithy shape ``com.amazonaws.lakeformation#OptimizerType``."""

from typing import Literal, TypeAlias, cast

OptimizerType: TypeAlias = Literal[
    "COMPACTION",
    "GARBAGE_COLLECTION",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: OptimizerType) -> str:
    return value


def deserialize_json(data: str) -> OptimizerType:
    return cast(OptimizerType, data)
