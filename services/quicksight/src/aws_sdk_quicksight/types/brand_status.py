"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandStatus``."""

from typing import Literal, TypeAlias, cast

BrandStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCEEDED",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrandStatus) -> str:
    return value


def deserialize_json(data: str) -> BrandStatus:
    return cast(BrandStatus, data)
