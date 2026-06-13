"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UsageAmounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.usage_amount

UsageAmounts: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.usage_amount.UsageAmount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageAmounts) -> list:
    import aws_sdk_bcm_pricing_calculator.types.usage_amount

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.usage_amount.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> UsageAmounts:
    import aws_sdk_bcm_pricing_calculator.types.usage_amount

    out: UsageAmounts = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.usage_amount.deserialize_aws_json_1_0(
                item
            )
        )
    return out
