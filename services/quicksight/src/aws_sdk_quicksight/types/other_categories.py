"""Generated from Smithy shape ``com.amazonaws.quicksight#OtherCategories``."""

from typing import Literal, TypeAlias, cast

OtherCategories: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: OtherCategories) -> str:
    return value


def deserialize_json(data: str) -> OtherCategories:
    return cast(OtherCategories, data)
