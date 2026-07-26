"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansUtilizationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.attributes
    import capo_cost_explorer.types.savings_plan_arn
    import capo_cost_explorer.types.savings_plans_amortized_commitment
    import capo_cost_explorer.types.savings_plans_savings
    import capo_cost_explorer.types.savings_plans_utilization


class SavingsPlansUtilizationDetail(TypedDict, closed=True):
    savings_plan_arn: NotRequired[
        "capo_cost_explorer.types.savings_plan_arn.SavingsPlanArn"
    ]
    """<p>The unique Amazon Resource Name (ARN) for a particular Savings Plan.</p>"""
    attributes: NotRequired["capo_cost_explorer.types.attributes.Attributes"]
    """<p>The attribute that applies to a specific <code>Dimension</code>.</p>"""
    utilization: NotRequired[
        "capo_cost_explorer.types.savings_plans_utilization.SavingsPlansUtilization"
    ]
    """<p>A ratio of your effectiveness of using existing Savings Plans to apply to workloads that are Savings Plans eligible.</p>"""
    savings: NotRequired[
        "capo_cost_explorer.types.savings_plans_savings.SavingsPlansSavings"
    ]
    """<p>The amount saved by using existing Savings Plans. Savings returns both net savings from savings plans and also the <code>onDemandCostEquivalent</code> of the Savings Plans when considering the utilization rate.</p>"""
    amortized_commitment: NotRequired[
        "capo_cost_explorer.types.savings_plans_amortized_commitment.SavingsPlansAmortizedCommitment"
    ]
    """<p>The total amortized commitment for a Savings Plans. Includes the sum of the upfront and recurring Savings Plans fees.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansUtilizationDetail) -> dict:
    out: dict = {}
    if "savings_plan_arn" in value:
        out["SavingsPlanArn"] = value["savings_plan_arn"]
    if "attributes" in value:
        import capo_cost_explorer.types.attributes

        out["Attributes"] = capo_cost_explorer.types.attributes.serialize_aws_json_1_1(
            value["attributes"]
        )
    if "utilization" in value:
        import capo_cost_explorer.types.savings_plans_utilization

        out["Utilization"] = (
            capo_cost_explorer.types.savings_plans_utilization.serialize_aws_json_1_1(
                value["utilization"]
            )
        )
    if "savings" in value:
        import capo_cost_explorer.types.savings_plans_savings

        out["Savings"] = (
            capo_cost_explorer.types.savings_plans_savings.serialize_aws_json_1_1(
                value["savings"]
            )
        )
    if "amortized_commitment" in value:
        import capo_cost_explorer.types.savings_plans_amortized_commitment

        out["AmortizedCommitment"] = (
            capo_cost_explorer.types.savings_plans_amortized_commitment.serialize_aws_json_1_1(
                value["amortized_commitment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansUtilizationDetail:
    out: SavingsPlansUtilizationDetail = {}  # type: ignore[typeddict-item]
    if "SavingsPlanArn" in data:
        out["savings_plan_arn"] = data["SavingsPlanArn"]
    if "Attributes" in data:
        import capo_cost_explorer.types.attributes

        out["attributes"] = (
            capo_cost_explorer.types.attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    if "Utilization" in data:
        import capo_cost_explorer.types.savings_plans_utilization

        out["utilization"] = (
            capo_cost_explorer.types.savings_plans_utilization.deserialize_aws_json_1_1(
                data["Utilization"]
            )
        )
    if "Savings" in data:
        import capo_cost_explorer.types.savings_plans_savings

        out["savings"] = (
            capo_cost_explorer.types.savings_plans_savings.deserialize_aws_json_1_1(
                data["Savings"]
            )
        )
    if "AmortizedCommitment" in data:
        import capo_cost_explorer.types.savings_plans_amortized_commitment

        out["amortized_commitment"] = (
            capo_cost_explorer.types.savings_plans_amortized_commitment.deserialize_aws_json_1_1(
                data["AmortizedCommitment"]
            )
        )
    return out
