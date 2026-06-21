"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteRackUseType``."""

from typing import Literal, TypeAlias, cast

QuoteRackUseType: TypeAlias = Literal[
    "NETWORKING",
    "COMPUTE",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteRackUseType) -> str:
    return value


def deserialize_json(data: str) -> QuoteRackUseType:
    return cast(QuoteRackUseType, data)
