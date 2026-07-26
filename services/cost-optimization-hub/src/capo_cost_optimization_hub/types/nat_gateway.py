"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#NatGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.nat_gateway_configuration
    import capo_cost_optimization_hub.types.resource_cost_calculation


class NatGateway(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_cost_optimization_hub.types.nat_gateway_configuration.NatGatewayConfiguration"
    ]
    """<p>The NAT Gateway configuration used for recommendations.</p>"""
    cost_calculation: NotRequired[
        "capo_cost_optimization_hub.types.resource_cost_calculation.ResourceCostCalculation"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGateway) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_cost_optimization_hub.types.nat_gateway_configuration

        out["configuration"] = (
            capo_cost_optimization_hub.types.nat_gateway_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "cost_calculation" in value:
        import capo_cost_optimization_hub.types.resource_cost_calculation

        out["costCalculation"] = (
            capo_cost_optimization_hub.types.resource_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NatGateway:
    out: NatGateway = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import capo_cost_optimization_hub.types.nat_gateway_configuration

        out["configuration"] = (
            capo_cost_optimization_hub.types.nat_gateway_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "costCalculation" in data:
        import capo_cost_optimization_hub.types.resource_cost_calculation

        out["cost_calculation"] = (
            capo_cost_optimization_hub.types.resource_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
