"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandVersionStatus``."""

from typing import Literal, TypeAlias, cast

BrandVersionStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCEEDED",
    "CREATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrandVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> BrandVersionStatus:
    return cast(BrandVersionStatus, data)
