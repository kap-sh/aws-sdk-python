"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#Format``."""

from typing import Literal, TypeAlias, cast

Format: TypeAlias = Literal[
    "CSV",
    "PARQUET",
]


# --- restJson1 ser/de ---
def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    return cast(Format, data)
