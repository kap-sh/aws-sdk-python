"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#DocumentDbCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.resource_cost_calculation


class DocumentDbCluster(TypedDict, closed=True):
    cost_calculation: NotRequired[
        "capo_cost_optimization_hub.types.resource_cost_calculation.ResourceCostCalculation"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DocumentDbCluster) -> dict:
    out: dict = {}
    if "cost_calculation" in value:
        import capo_cost_optimization_hub.types.resource_cost_calculation

        out["costCalculation"] = (
            capo_cost_optimization_hub.types.resource_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DocumentDbCluster:
    out: DocumentDbCluster = {}  # type: ignore[typeddict-item]
    if "costCalculation" in data:
        import capo_cost_optimization_hub.types.resource_cost_calculation

        out["cost_calculation"] = (
            capo_cost_optimization_hub.types.resource_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
