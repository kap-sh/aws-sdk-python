"""Generated from Smithy shape ``com.amazonaws.quicksight#ResizeOption``."""

from typing import Literal, TypeAlias, cast

ResizeOption: TypeAlias = Literal[
    "FIXED",
    "RESPONSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResizeOption) -> str:
    return value


def deserialize_json(data: str) -> ResizeOption:
    return cast(ResizeOption, data)
