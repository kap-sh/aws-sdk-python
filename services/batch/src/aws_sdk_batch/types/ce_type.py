"""Generated from Smithy shape ``com.amazonaws.batch#CEType``."""

from typing import Literal, TypeAlias, cast

CEType: TypeAlias = Literal[
    "MANAGED",
    "UNMANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CEType) -> str:
    return value


def deserialize_json(data: str) -> CEType:
    return cast(CEType, data)
