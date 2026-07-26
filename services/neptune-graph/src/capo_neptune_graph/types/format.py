"""Generated from Smithy shape ``com.amazonaws.neptunegraph#Format``."""

from typing import Literal, TypeAlias, cast

Format: TypeAlias = Literal[
    "CSV",
    "OPEN_CYPHER",
    "PARQUET",
    "NTRIPLES",
]


# --- restJson1 ser/de ---
def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    return cast(Format, data)
