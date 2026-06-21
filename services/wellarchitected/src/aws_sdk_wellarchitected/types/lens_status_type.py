"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensStatusType``."""

from typing import Literal, TypeAlias, cast

LensStatusType: TypeAlias = Literal[
    "ALL",
    "DRAFT",
    "PUBLISHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LensStatusType) -> str:
    return value


def deserialize_json(data: str) -> LensStatusType:
    return cast(LensStatusType, data)
