"""Generated from Smithy shape ``com.amazonaws.datazone#ChangeAction``."""

from typing import Literal, TypeAlias, cast

ChangeAction: TypeAlias = Literal[
    "PUBLISH",
    "UNPUBLISH",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeAction) -> str:
    return value


def deserialize_json(data: str) -> ChangeAction:
    return cast(ChangeAction, data)
