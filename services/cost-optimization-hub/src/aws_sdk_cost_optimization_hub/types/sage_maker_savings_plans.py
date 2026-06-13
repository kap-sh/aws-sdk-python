"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#SageMakerSavingsPlans``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans_configuration
    import aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation


class SageMakerSavingsPlans(TypedDict):
    configuration: NotRequired[
        "aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans_configuration.SageMakerSavingsPlansConfiguration"
    ]
    """<p>The SageMaker Savings Plans configuration used for recommendations.</p>"""
    cost_calculation: NotRequired[
        "aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation.SavingsPlansCostCalculation"
    ]
    """<p>Cost impact of the Savings Plans purchase recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SageMakerSavingsPlans) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "cost_calculation" in value:
        import aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation

        out["costCalculation"] = (
            aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SageMakerSavingsPlans:
    out: SageMakerSavingsPlans = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "costCalculation" in data:
        import aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation

        out["cost_calculation"] = (
            aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
