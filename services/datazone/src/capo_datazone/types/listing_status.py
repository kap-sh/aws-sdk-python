"""Generated from Smithy shape ``com.amazonaws.datazone#ListingStatus``."""

from typing import Literal, TypeAlias, cast

ListingStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingStatus) -> str:
    return value


def deserialize_json(data: str) -> ListingStatus:
    return cast(ListingStatus, data)
