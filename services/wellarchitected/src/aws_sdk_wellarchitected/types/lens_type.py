"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensType``."""

from typing import Literal, TypeAlias, cast

LensType: TypeAlias = Literal[
    "AWS_OFFICIAL",
    "CUSTOM_SHARED",
    "CUSTOM_SELF",
]


# --- restJson1 ser/de ---
def serialize_json(value: LensType) -> str:
    return value


def deserialize_json(data: str) -> LensType:
    return cast(LensType, data)
