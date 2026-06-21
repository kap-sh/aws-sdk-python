"""Generated from Smithy shape ``com.amazonaws.outposts#LineItemStatus``."""

from typing import Literal, TypeAlias, cast

LineItemStatus: TypeAlias = Literal[
    "PREPARING",
    "BUILDING",
    "SHIPPED",
    "DELIVERED",
    "INSTALLING",
    "INSTALLED",
    "ERROR",
    "CANCELLED",
    "REPLACED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemStatus) -> str:
    return value


def deserialize_json(data: str) -> LineItemStatus:
    return cast(LineItemStatus, data)
