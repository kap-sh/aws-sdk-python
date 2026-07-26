"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteConstraintType``."""

from typing import Literal, TypeAlias, cast

QuoteConstraintType: TypeAlias = Literal[
    "RACK_MAXIMUM",
    "RACK_MAX_POWER_KVA",
    "RACK_MAX_WEIGHT_LBS",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteConstraintType) -> str:
    return value


def deserialize_json(data: str) -> QuoteConstraintType:
    return cast(QuoteConstraintType, data)
