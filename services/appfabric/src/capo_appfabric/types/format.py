"""Generated from Smithy shape ``com.amazonaws.appfabric#Format``."""

from typing import Literal, TypeAlias, cast

Format: TypeAlias = Literal[
    "json",
    "parquet",
]


# --- restJson1 ser/de ---
def serialize_json(value: Format) -> str:
    return value


def deserialize_json(data: str) -> Format:
    return cast(Format, data)
