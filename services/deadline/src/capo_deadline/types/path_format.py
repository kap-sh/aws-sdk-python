"""Generated from Smithy shape ``com.amazonaws.deadline#PathFormat``."""

from typing import Literal, TypeAlias, cast

PathFormat: TypeAlias = Literal[
    "windows",
    "posix",
]


# --- restJson1 ser/de ---
def serialize_json(value: PathFormat) -> str:
    return value


def deserialize_json(data: str) -> PathFormat:
    return cast(PathFormat, data)
