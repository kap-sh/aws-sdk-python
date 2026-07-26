"""Generated from Smithy shape ``com.amazonaws.quicksight#Role``."""

from typing import Literal, TypeAlias, cast

Role: TypeAlias = Literal[
    "ADMIN",
    "AUTHOR",
    "READER",
    "ADMIN_PRO",
    "AUTHOR_PRO",
    "READER_PRO",
]


# --- restJson1 ser/de ---
def serialize_json(value: Role) -> str:
    return value


def deserialize_json(data: str) -> Role:
    return cast(Role, data)
