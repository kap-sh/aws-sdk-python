"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#WorkSpaces``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.resource_cost_calculation


class WorkSpaces(TypedDict):
    cost_calculation: NotRequired[
        "aws_sdk_cost_optimization_hub.types.resource_cost_calculation.ResourceCostCalculation"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkSpaces) -> dict:
    out: dict = {}
    if "cost_calculation" in value:
        import aws_sdk_cost_optimization_hub.types.resource_cost_calculation

        out["costCalculation"] = (
            aws_sdk_cost_optimization_hub.types.resource_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkSpaces:
    out: WorkSpaces = {}  # type: ignore[typeddict-item]
    if "costCalculation" in data:
        import aws_sdk_cost_optimization_hub.types.resource_cost_calculation

        out["cost_calculation"] = (
            aws_sdk_cost_optimization_hub.types.resource_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
