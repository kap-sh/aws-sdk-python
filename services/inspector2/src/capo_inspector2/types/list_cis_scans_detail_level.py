"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScansDetailLevel``."""

from typing import Literal, TypeAlias, cast

ListCisScansDetailLevel: TypeAlias = Literal[
    "ORGANIZATION",
    "MEMBER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScansDetailLevel) -> str:
    return value


def deserialize_json(data: str) -> ListCisScansDetailLevel:
    return cast(ListCisScansDetailLevel, data)
