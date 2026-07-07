"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSInstanceSavingsOpportunityAfterDiscounts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.rds_instance_estimated_monthly_savings
    import aws_sdk_compute_optimizer.types.savings_opportunity_percentage


class RDSInstanceSavingsOpportunityAfterDiscounts(TypedDict, closed=True):
    savings_opportunity_percentage: "aws_sdk_compute_optimizer.types.savings_opportunity_percentage.SavingsOpportunityPercentage"
    """<p> The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer’s DB instance recommendations. This includes any applicable Savings Plans discounts. </p>"""
    estimated_monthly_savings: NotRequired[
        "aws_sdk_compute_optimizer.types.rds_instance_estimated_monthly_savings.RDSInstanceEstimatedMonthlySavings"
    ]
    """<p> The estimated monthly savings possible by adopting Compute Optimizer’s DB instance recommendations. This includes any applicable Savings Plans discounts. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSInstanceSavingsOpportunityAfterDiscounts) -> dict:
    out: dict = {}
    out["savingsOpportunityPercentage"] = value.get("savings_opportunity_percentage", 0)
    if "estimated_monthly_savings" in value:
        import aws_sdk_compute_optimizer.types.rds_instance_estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            aws_sdk_compute_optimizer.types.rds_instance_estimated_monthly_savings.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSInstanceSavingsOpportunityAfterDiscounts:
    out: RDSInstanceSavingsOpportunityAfterDiscounts = {}  # type: ignore[typeddict-item]
    if "savingsOpportunityPercentage" in data:
        out["savings_opportunity_percentage"] = data["savingsOpportunityPercentage"]
    else:
        out["savings_opportunity_percentage"] = 0
    if "estimatedMonthlySavings" in data:
        import aws_sdk_compute_optimizer.types.rds_instance_estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            aws_sdk_compute_optimizer.types.rds_instance_estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    return out
