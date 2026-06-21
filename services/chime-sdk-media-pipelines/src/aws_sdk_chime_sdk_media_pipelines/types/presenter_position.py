"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#PresenterPosition``."""

from typing import Literal, TypeAlias, cast

PresenterPosition: TypeAlias = Literal[
    "TopLeft",
    "TopRight",
    "BottomLeft",
    "BottomRight",
]


# --- restJson1 ser/de ---
def serialize_json(value: PresenterPosition) -> str:
    return value


def deserialize_json(data: str) -> PresenterPosition:
    return cast(PresenterPosition, data)
