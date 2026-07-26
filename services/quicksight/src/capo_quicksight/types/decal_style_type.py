"""Generated from Smithy shape ``com.amazonaws.quicksight#DecalStyleType``."""

from typing import Literal, TypeAlias, cast

DecalStyleType: TypeAlias = Literal[
    "Manual",
    "Auto",
]


# --- restJson1 ser/de ---
def serialize_json(value: DecalStyleType) -> str:
    return value


def deserialize_json(data: str) -> DecalStyleType:
    return cast(DecalStyleType, data)
