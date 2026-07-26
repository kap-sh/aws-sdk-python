"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UsageAmounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.usage_amount

UsageAmounts: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.usage_amount.UsageAmount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageAmounts) -> list:
    import capo_bcm_pricing_calculator.types.usage_amount

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.usage_amount.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> UsageAmounts:
    import capo_bcm_pricing_calculator.types.usage_amount

    out: UsageAmounts = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.usage_amount.deserialize_aws_json_1_0(
                item
            )
        )
    return out
