"""Generated from Smithy shape ``com.amazonaws.billingconductor#LineItemFilterAttributeName``."""

from typing import Literal, TypeAlias, cast

LineItemFilterAttributeName: TypeAlias = Literal[
    "LINE_ITEM_TYPE",
    "SERVICE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemFilterAttributeName) -> str:
    return value


def deserialize_json(data: str) -> LineItemFilterAttributeName:
    return cast(LineItemFilterAttributeName, data)
