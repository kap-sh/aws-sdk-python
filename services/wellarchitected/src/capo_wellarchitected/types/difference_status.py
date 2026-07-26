"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DifferenceStatus``."""

from typing import Literal, TypeAlias, cast

DifferenceStatus: TypeAlias = Literal[
    "UPDATED",
    "NEW",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DifferenceStatus) -> str:
    return value


def deserialize_json(data: str) -> DifferenceStatus:
    return cast(DifferenceStatus, data)
