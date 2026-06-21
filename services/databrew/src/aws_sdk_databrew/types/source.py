"""Generated from Smithy shape ``com.amazonaws.databrew#Source``."""

from typing import Literal, TypeAlias, cast

Source: TypeAlias = Literal[
    "S3",
    "DATA-CATALOG",
    "DATABASE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> str:
    return value


def deserialize_json(data: str) -> Source:
    return cast(Source, data)
