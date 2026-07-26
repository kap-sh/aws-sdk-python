"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ServiceCostDifferenceMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.cost_difference

ServiceCostDifferenceMap: TypeAlias = dict[
    "str", "capo_bcm_pricing_calculator.types.cost_difference.CostDifference"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ServiceCostDifferenceMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bcm_pricing_calculator.types.cost_difference

        out[key] = (
            capo_bcm_pricing_calculator.types.cost_difference.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceCostDifferenceMap:
    out: ServiceCostDifferenceMap = {}
    for key, value in data.items():
        import capo_bcm_pricing_calculator.types.cost_difference

        out[key] = (
            capo_bcm_pricing_calculator.types.cost_difference.deserialize_aws_json_1_0(
                value
            )
        )
    return out
