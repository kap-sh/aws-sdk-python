"""Generated from Smithy shape ``com.amazonaws.quicksight#BaseMapStyleType``."""

from typing import Literal, TypeAlias, cast

BaseMapStyleType: TypeAlias = Literal[
    "LIGHT_GRAY",
    "DARK_GRAY",
    "STREET",
    "IMAGERY",
]


# --- restJson1 ser/de ---
def serialize_json(value: BaseMapStyleType) -> str:
    return value


def deserialize_json(data: str) -> BaseMapStyleType:
    return cast(BaseMapStyleType, data)
