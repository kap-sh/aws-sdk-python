"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansUtilizationByTime``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.savings_plans_amortized_commitment
    import aws_sdk_cost_explorer.types.savings_plans_savings
    import aws_sdk_cost_explorer.types.savings_plans_utilization


class SavingsPlansUtilizationByTime(TypedDict):
    time_period: "aws_sdk_cost_explorer.types.date_interval.DateInterval"
    utilization: (
        "aws_sdk_cost_explorer.types.savings_plans_utilization.SavingsPlansUtilization"
    )
    """<p>A ratio of your effectiveness of using existing Savings Plans to apply to workloads that are Savings Plans eligible.</p>"""
    savings: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_savings.SavingsPlansSavings"
    ]
    """<p>The amount that's saved by using existing Savings Plans. Savings returns both net savings from Savings Plans and also the <code>onDemandCostEquivalent</code> of the Savings Plans when considering the utilization rate.</p>"""
    amortized_commitment: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_amortized_commitment.SavingsPlansAmortizedCommitment"
    ]
    """<p>The total amortized commitment for a Savings Plans. This includes the sum of the upfront and recurring Savings Plans fees.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansUtilizationByTime) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.date_interval

    out["TimePeriod"] = (
        aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
            value["time_period"]
        )
    )
    import aws_sdk_cost_explorer.types.savings_plans_utilization

    out["Utilization"] = (
        aws_sdk_cost_explorer.types.savings_plans_utilization.serialize_aws_json_1_1(
            value["utilization"]
        )
    )
    if "savings" in value:
        import aws_sdk_cost_explorer.types.savings_plans_savings

        out["Savings"] = (
            aws_sdk_cost_explorer.types.savings_plans_savings.serialize_aws_json_1_1(
                value["savings"]
            )
        )
    if "amortized_commitment" in value:
        import aws_sdk_cost_explorer.types.savings_plans_amortized_commitment

        out["AmortizedCommitment"] = (
            aws_sdk_cost_explorer.types.savings_plans_amortized_commitment.serialize_aws_json_1_1(
                value["amortized_commitment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansUtilizationByTime:
    out: SavingsPlansUtilizationByTime = {}  # type: ignore[typeddict-item]
    if "TimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError("SavingsPlansUtilizationByTime.time_period required")
    if "Utilization" in data:
        import aws_sdk_cost_explorer.types.savings_plans_utilization

        out["utilization"] = (
            aws_sdk_cost_explorer.types.savings_plans_utilization.deserialize_aws_json_1_1(
                data["Utilization"]
            )
        )
    else:
        raise DeserializationError("SavingsPlansUtilizationByTime.utilization required")
    if "Savings" in data:
        import aws_sdk_cost_explorer.types.savings_plans_savings

        out["savings"] = (
            aws_sdk_cost_explorer.types.savings_plans_savings.deserialize_aws_json_1_1(
                data["Savings"]
            )
        )
    if "AmortizedCommitment" in data:
        import aws_sdk_cost_explorer.types.savings_plans_amortized_commitment

        out["amortized_commitment"] = (
            aws_sdk_cost_explorer.types.savings_plans_amortized_commitment.deserialize_aws_json_1_1(
                data["AmortizedCommitment"]
            )
        )
    return out
