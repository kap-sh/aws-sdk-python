"""Generated from Smithy shape ``com.amazonaws.finspace#ChangeType``."""

from typing import Literal, TypeAlias, cast

ChangeType: TypeAlias = Literal[
    "PUT",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeType) -> str:
    return value


def deserialize_json(data: str) -> ChangeType:
    return cast(ChangeType, data)
