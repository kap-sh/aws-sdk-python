"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceType``."""

from typing import Literal, TypeAlias, cast

"""Used in SdiSource, CreateSdiSourceRequest, UpdateSdiSourceRequest."""
SdiSourceType: TypeAlias = Literal[
    "SINGLE",
    "QUAD",
]


# --- restJson1 ser/de ---
def serialize_json(value: SdiSourceType) -> str:
    return value


def deserialize_json(data: str) -> SdiSourceType:
    return cast(SdiSourceType, data)
