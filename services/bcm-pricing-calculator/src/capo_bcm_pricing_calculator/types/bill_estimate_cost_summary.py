"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateCostSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.cost_difference
    import capo_bcm_pricing_calculator.types.service_cost_difference_map


class BillEstimateCostSummary(TypedDict, closed=True):
    total_cost_difference: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_difference.CostDifference"
    ]
    """<p> The total difference in cost between the estimated and historical costs. </p>"""
    service_cost_differences: NotRequired[
        "capo_bcm_pricing_calculator.types.service_cost_difference_map.ServiceCostDifferenceMap"
    ]
    """<p> A breakdown of cost differences by Amazon Web Services service. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateCostSummary) -> dict:
    out: dict = {}
    if "total_cost_difference" in value:
        import capo_bcm_pricing_calculator.types.cost_difference

        out["totalCostDifference"] = (
            capo_bcm_pricing_calculator.types.cost_difference.serialize_aws_json_1_0(
                value["total_cost_difference"]
            )
        )
    if "service_cost_differences" in value:
        import capo_bcm_pricing_calculator.types.service_cost_difference_map

        out["serviceCostDifferences"] = (
            capo_bcm_pricing_calculator.types.service_cost_difference_map.serialize_aws_json_1_0(
                value["service_cost_differences"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillEstimateCostSummary:
    out: BillEstimateCostSummary = {}  # type: ignore[typeddict-item]
    if "totalCostDifference" in data:
        import capo_bcm_pricing_calculator.types.cost_difference

        out["total_cost_difference"] = (
            capo_bcm_pricing_calculator.types.cost_difference.deserialize_aws_json_1_0(
                data["totalCostDifference"]
            )
        )
    if "serviceCostDifferences" in data:
        import capo_bcm_pricing_calculator.types.service_cost_difference_map

        out["service_cost_differences"] = (
            capo_bcm_pricing_calculator.types.service_cost_difference_map.deserialize_aws_json_1_0(
                data["serviceCostDifferences"]
            )
        )
    return out
