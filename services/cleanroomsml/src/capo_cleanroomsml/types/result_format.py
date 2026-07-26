"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ResultFormat``."""

from typing import Literal, TypeAlias, cast

"""File format of the returned data."""
ResultFormat: TypeAlias = Literal[
    "CSV",
    "PARQUET",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResultFormat) -> str:
    return value


def deserialize_json(data: str) -> ResultFormat:
    return cast(ResultFormat, data)
