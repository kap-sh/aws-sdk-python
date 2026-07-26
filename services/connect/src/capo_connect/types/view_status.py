"""Generated from Smithy shape ``com.amazonaws.connect#ViewStatus``."""

from typing import Literal, TypeAlias, cast

ViewStatus: TypeAlias = Literal[
    "PUBLISHED",
    "SAVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ViewStatus) -> str:
    return value


def deserialize_json(data: str) -> ViewStatus:
    return cast(ViewStatus, data)
