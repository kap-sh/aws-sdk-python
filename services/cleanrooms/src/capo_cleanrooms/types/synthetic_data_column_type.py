"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SyntheticDataColumnType``."""

from typing import Literal, TypeAlias, cast

SyntheticDataColumnType: TypeAlias = Literal[
    "CATEGORICAL",
    "NUMERICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: SyntheticDataColumnType) -> str:
    return value


def deserialize_json(data: str) -> SyntheticDataColumnType:
    return cast(SyntheticDataColumnType, data)
