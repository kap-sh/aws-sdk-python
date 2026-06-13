"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ServiceCostDifferenceMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.cost_difference

ServiceCostDifferenceMap: TypeAlias = dict[
    "str", "aws_sdk_bcm_pricing_calculator.types.cost_difference.CostDifference"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ServiceCostDifferenceMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bcm_pricing_calculator.types.cost_difference

        out[key] = (
            aws_sdk_bcm_pricing_calculator.types.cost_difference.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceCostDifferenceMap:
    out: ServiceCostDifferenceMap = {}
    for key, value in data.items():
        import aws_sdk_bcm_pricing_calculator.types.cost_difference

        out[key] = (
            aws_sdk_bcm_pricing_calculator.types.cost_difference.deserialize_aws_json_1_0(
                value
            )
        )
    return out
