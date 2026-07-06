"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#OpenSearchReservedInstances``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.open_search_reserved_instances_configuration
    import aws_sdk_cost_optimization_hub.types.reserved_instances_cost_calculation


class OpenSearchReservedInstances(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_cost_optimization_hub.types.open_search_reserved_instances_configuration.OpenSearchReservedInstancesConfiguration"
    ]
    """<p>The OpenSearch reserved instances configuration used for recommendations.</p>"""
    cost_calculation: NotRequired[
        "aws_sdk_cost_optimization_hub.types.reserved_instances_cost_calculation.ReservedInstancesCostCalculation"
    ]
    """<p>Cost impact of the purchase recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenSearchReservedInstances) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_cost_optimization_hub.types.open_search_reserved_instances_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.open_search_reserved_instances_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "cost_calculation" in value:
        import aws_sdk_cost_optimization_hub.types.reserved_instances_cost_calculation

        out["costCalculation"] = (
            aws_sdk_cost_optimization_hub.types.reserved_instances_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpenSearchReservedInstances:
    out: OpenSearchReservedInstances = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_cost_optimization_hub.types.open_search_reserved_instances_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.open_search_reserved_instances_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "costCalculation" in data:
        import aws_sdk_cost_optimization_hub.types.reserved_instances_cost_calculation

        out["cost_calculation"] = (
            aws_sdk_cost_optimization_hub.types.reserved_instances_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
