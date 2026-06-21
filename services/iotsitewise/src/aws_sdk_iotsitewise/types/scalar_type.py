"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ScalarType``."""

from typing import Literal, TypeAlias, cast

ScalarType: TypeAlias = Literal[
    "BOOLEAN",
    "INT",
    "DOUBLE",
    "TIMESTAMP",
    "STRING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScalarType) -> str:
    return value


def deserialize_json(data: str) -> ScalarType:
    return cast(ScalarType, data)
