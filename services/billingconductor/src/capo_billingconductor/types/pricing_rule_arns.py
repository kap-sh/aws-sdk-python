"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingRuleArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.pricing_rule_arn

PricingRuleArns: TypeAlias = list[
    "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingRuleArns) -> list:
    return list(value)


def deserialize_json(data: list) -> PricingRuleArns:
    return list(data)
