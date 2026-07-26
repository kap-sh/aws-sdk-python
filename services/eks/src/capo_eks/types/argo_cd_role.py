"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdRole``."""

from typing import Literal, TypeAlias, cast

ArgoCdRole: TypeAlias = Literal[
    "ADMIN",
    "EDITOR",
    "VIEWER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdRole) -> str:
    return value


def deserialize_json(data: str) -> ArgoCdRole:
    return cast(ArgoCdRole, data)
