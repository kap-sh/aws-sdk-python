"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingRuleArnsNonEmptyInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_rule_arn

PricingRuleArnsNonEmptyInput: TypeAlias = list[
    "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingRuleArnsNonEmptyInput) -> list:
    return list(value)


def deserialize_json(data: list) -> PricingRuleArnsNonEmptyInput:
    return list(data)
