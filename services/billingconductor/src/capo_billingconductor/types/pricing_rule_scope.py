"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingRuleScope``."""

from typing import Literal, TypeAlias, cast

PricingRuleScope: TypeAlias = Literal[
    "GLOBAL",
    "SERVICE",
    "BILLING_ENTITY",
    "SKU",
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingRuleScope) -> str:
    return value


def deserialize_json(data: str) -> PricingRuleScope:
    return cast(PricingRuleScope, data)
