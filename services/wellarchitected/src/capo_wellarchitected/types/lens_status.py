"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensStatus``."""

from typing import Literal, TypeAlias, cast

LensStatus: TypeAlias = Literal[
    "CURRENT",
    "NOT_CURRENT",
    "DEPRECATED",
    "DELETED",
    "UNSHARED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LensStatus) -> str:
    return value


def deserialize_json(data: str) -> LensStatus:
    return cast(LensStatus, data)
