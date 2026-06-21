"""Generated from Smithy shape ``com.amazonaws.networkmanager#ChangeAction``."""

from typing import Literal, TypeAlias, cast

ChangeAction: TypeAlias = Literal[
    "ADD",
    "MODIFY",
    "REMOVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeAction) -> str:
    return value


def deserialize_json(data: str) -> ChangeAction:
    return cast(ChangeAction, data)
