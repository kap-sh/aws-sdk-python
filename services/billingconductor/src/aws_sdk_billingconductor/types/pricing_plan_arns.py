"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingPlanArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_plan_arn

PricingPlanArns: TypeAlias = list[
    "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingPlanArns) -> list:
    return list(value)


def deserialize_json(data: list) -> PricingPlanArns:
    return list(data)
