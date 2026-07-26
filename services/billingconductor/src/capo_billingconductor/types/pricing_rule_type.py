"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingRuleType``."""

from typing import Literal, TypeAlias, cast

PricingRuleType: TypeAlias = Literal[
    "MARKUP",
    "DISCOUNT",
    "TIERING",
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingRuleType) -> str:
    return value


def deserialize_json(data: str) -> PricingRuleType:
    return cast(PricingRuleType, data)
