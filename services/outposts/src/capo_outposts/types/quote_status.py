"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteStatus``."""

from typing import Literal, TypeAlias, cast

QuoteStatus: TypeAlias = Literal[
    "CREATED",
    "ORDER_SUBMITTED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteStatus) -> str:
    return value


def deserialize_json(data: str) -> QuoteStatus:
    return cast(QuoteStatus, data)
