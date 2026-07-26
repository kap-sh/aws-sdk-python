"""Generated from Smithy shape ``com.amazonaws.outposts#PricingResult``."""

from typing import Literal, TypeAlias, cast

PricingResult: TypeAlias = Literal[
    "PRICED",
    "UNABLE_TO_PRICE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingResult) -> str:
    return value


def deserialize_json(data: str) -> PricingResult:
    return cast(PricingResult, data)
