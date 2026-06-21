"""Generated from Smithy shape ``com.amazonaws.repostspace#Role``."""

from typing import Literal, TypeAlias, cast

Role: TypeAlias = Literal[
    "EXPERT",
    "MODERATOR",
    "ADMINISTRATOR",
    "SUPPORTREQUESTOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: Role) -> str:
    return value


def deserialize_json(data: str) -> Role:
    return cast(Role, data)
