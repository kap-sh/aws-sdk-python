"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RdsDbInstance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.rds_db_instance_configuration
    import aws_sdk_cost_optimization_hub.types.resource_cost_calculation


class RdsDbInstance(TypedDict):
    configuration: NotRequired[
        "aws_sdk_cost_optimization_hub.types.rds_db_instance_configuration.RdsDbInstanceConfiguration"
    ]
    """<p>The Amazon RDS DB instance configuration used for recommendations.</p>"""
    cost_calculation: NotRequired[
        "aws_sdk_cost_optimization_hub.types.resource_cost_calculation.ResourceCostCalculation"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RdsDbInstance) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_cost_optimization_hub.types.rds_db_instance_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.rds_db_instance_configuration.serialize_aws_json_1_0(
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


def deserialize_aws_json_1_0(data: dict) -> RdsDbInstance:
    out: RdsDbInstance = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_cost_optimization_hub.types.rds_db_instance_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.rds_db_instance_configuration.deserialize_aws_json_1_0(
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
