"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#EcsService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.ecs_service_configuration
    import aws_sdk_cost_optimization_hub.types.resource_cost_calculation


class EcsService(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_cost_optimization_hub.types.ecs_service_configuration.EcsServiceConfiguration"
    ]
    """<p>The ECS service configuration used for recommendations.</p>"""
    cost_calculation: NotRequired[
        "aws_sdk_cost_optimization_hub.types.resource_cost_calculation.ResourceCostCalculation"
    ]
    """<p>Cost impact of the recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EcsService) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_cost_optimization_hub.types.ecs_service_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.ecs_service_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "cost_calculation" in value:
        import aws_sdk_cost_optimization_hub.types.resource_cost_calculation

        out["costCalculation"] = (
            aws_sdk_cost_optimization_hub.types.resource_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EcsService:
    out: EcsService = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_cost_optimization_hub.types.ecs_service_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.ecs_service_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "costCalculation" in data:
        import aws_sdk_cost_optimization_hub.types.resource_cost_calculation

        out["cost_calculation"] = (
            aws_sdk_cost_optimization_hub.types.resource_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
