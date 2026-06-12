"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingRuleArnsInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_rule_arn

PricingRuleArnsInput: TypeAlias = list[
    "aws_sdk_billingconductor.types.pricing_rule_arn.PricingRuleArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingRuleArnsInput) -> list:
    return list(value)


def deserialize_json(data: list) -> PricingRuleArnsInput:
    return list(data)
