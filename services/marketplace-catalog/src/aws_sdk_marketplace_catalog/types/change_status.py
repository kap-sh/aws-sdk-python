"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ChangeStatus``."""

from typing import Literal, TypeAlias, cast

ChangeStatus: TypeAlias = Literal[
    "PREPARING",
    "APPLYING",
    "SUCCEEDED",
    "CANCELLED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeStatus) -> str:
    return value


def deserialize_json(data: str) -> ChangeStatus:
    return cast(ChangeStatus, data)
