"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DetailLevel``."""

from typing import Literal, TypeAlias, cast

DetailLevel: TypeAlias = Literal[
    "BRIEF",
    "DETAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DetailLevel) -> str:
    return value


def deserialize_json(data: str) -> DetailLevel:
    return cast(DetailLevel, data)
