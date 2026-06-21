"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Order``."""

from typing import Literal, TypeAlias, cast

"""Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource."""
Order: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: Order) -> str:
    return value


def deserialize_json(data: str) -> Order:
    return cast(Order, data)
