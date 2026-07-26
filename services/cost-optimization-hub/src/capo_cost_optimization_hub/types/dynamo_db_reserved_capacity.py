"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#DynamoDbReservedCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.dynamo_db_reserved_capacity_configuration
    import capo_cost_optimization_hub.types.reserved_instances_cost_calculation


class DynamoDbReservedCapacity(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_cost_optimization_hub.types.dynamo_db_reserved_capacity_configuration.DynamoDbReservedCapacityConfiguration"
    ]
    """<p>The DynamoDB reserved capacity configuration used for recommendations.</p>"""
    cost_calculation: NotRequired[
        "capo_cost_optimization_hub.types.reserved_instances_cost_calculation.ReservedInstancesCostCalculation"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DynamoDbReservedCapacity) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_cost_optimization_hub.types.dynamo_db_reserved_capacity_configuration

        out["configuration"] = (
            capo_cost_optimization_hub.types.dynamo_db_reserved_capacity_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "cost_calculation" in value:
        import capo_cost_optimization_hub.types.reserved_instances_cost_calculation

        out["costCalculation"] = (
            capo_cost_optimization_hub.types.reserved_instances_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DynamoDbReservedCapacity:
    out: DynamoDbReservedCapacity = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import capo_cost_optimization_hub.types.dynamo_db_reserved_capacity_configuration

        out["configuration"] = (
            capo_cost_optimization_hub.types.dynamo_db_reserved_capacity_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "costCalculation" in data:
        import capo_cost_optimization_hub.types.reserved_instances_cost_calculation

        out["cost_calculation"] = (
            capo_cost_optimization_hub.types.reserved_instances_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
