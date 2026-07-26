"""Generated from Smithy shape ``com.amazonaws.detective#Field``."""

from typing import Literal, TypeAlias, cast

Field: TypeAlias = Literal[
    "SEVERITY",
    "STATUS",
    "CREATED_TIME",
]


# --- restJson1 ser/de ---
def serialize_json(value: Field) -> str:
    return value


def deserialize_json(data: str) -> Field:
    return cast(Field, data)
