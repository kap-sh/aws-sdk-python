"""Generated from Smithy shape ``com.amazonaws.neptunedata#Mode``."""

from typing import Literal, TypeAlias, cast

Mode: TypeAlias = Literal[
    "RESUME",
    "NEW",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mode) -> str:
    return value


def deserialize_json(data: str) -> Mode:
    return cast(Mode, data)
