"""Generated from Smithy shape ``com.amazonaws.databrew#InputFormat``."""

from typing import Literal, TypeAlias, cast

InputFormat: TypeAlias = Literal[
    "CSV",
    "JSON",
    "PARQUET",
    "EXCEL",
    "ORC",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputFormat) -> str:
    return value


def deserialize_json(data: str) -> InputFormat:
    return cast(InputFormat, data)
