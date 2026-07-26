"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UsageQuantities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.usage_quantity

UsageQuantities: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.usage_quantity.UsageQuantity"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageQuantities) -> list:
    import capo_bcm_pricing_calculator.types.usage_quantity

    out: list = []
    for item in value:
        out.append(
            capo_bcm_pricing_calculator.types.usage_quantity.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> UsageQuantities:
    import capo_bcm_pricing_calculator.types.usage_quantity

    out: UsageQuantities = []
    for item in data:
        out.append(
            capo_bcm_pricing_calculator.types.usage_quantity.deserialize_aws_json_1_0(
                item
            )
        )
    return out
