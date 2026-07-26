"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingModelType``."""

from typing import Literal, TypeAlias, cast

PricingModelType: TypeAlias = Literal[
    "USAGE",
    "CONTRACT",
    "BYOL",
    "FREE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingModelType) -> str:
    return value


def deserialize_json(data: str) -> PricingModelType:
    return cast(PricingModelType, data)
