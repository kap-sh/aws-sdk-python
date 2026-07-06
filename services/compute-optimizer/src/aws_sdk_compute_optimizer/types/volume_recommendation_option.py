"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#VolumeRecommendationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ebs_savings_opportunity_after_discounts
    import aws_sdk_compute_optimizer.types.performance_risk
    import aws_sdk_compute_optimizer.types.rank
    import aws_sdk_compute_optimizer.types.savings_opportunity
    import aws_sdk_compute_optimizer.types.volume_configuration


class VolumeRecommendationOption(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_compute_optimizer.types.volume_configuration.VolumeConfiguration"
    ]
    """<p>An array of objects that describe a volume configuration.</p>"""
    performance_risk: "aws_sdk_compute_optimizer.types.performance_risk.PerformanceRisk"
    """<p>The performance risk of the volume recommendation option.</p> <p>Performance risk is the likelihood of the recommended volume type meeting the performance requirement of your workload.</p> <p>The value ranges from <code>0</code> - <code>4</code>, with <code>0</code> meaning that the recommended resource is predicted to always provide enough hardware capability. The higher the performance risk is, the more likely you should validate whether the recommendation will meet the performance requirements of your workload before migrating your resource.</p>"""
    rank: "aws_sdk_compute_optimizer.types.rank.Rank"
    """<p>The rank of the volume recommendation option.</p> <p>The top recommendation option is ranked as <code>1</code>.</p>"""
    savings_opportunity: NotRequired[
        "aws_sdk_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    """<p>An object that describes the savings opportunity for the EBS volume recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.</p>"""
    savings_opportunity_after_discounts: NotRequired[
        "aws_sdk_compute_optimizer.types.ebs_savings_opportunity_after_discounts.EBSSavingsOpportunityAfterDiscounts"
    ]
    """<p> An object that describes the savings opportunity for the Amazon EBS volume recommendation option with specific discounts. Savings opportunity includes the estimated monthly savings and percentage. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VolumeRecommendationOption) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_compute_optimizer.types.volume_configuration

        out["configuration"] = (
            aws_sdk_compute_optimizer.types.volume_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    out["performanceRisk"] = value.get("performance_risk", 0)
    out["rank"] = value.get("rank", 0)
    if "savings_opportunity" in value:
        import aws_sdk_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            aws_sdk_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import aws_sdk_compute_optimizer.types.ebs_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            aws_sdk_compute_optimizer.types.ebs_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VolumeRecommendationOption:
    out: VolumeRecommendationOption = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_compute_optimizer.types.volume_configuration

        out["configuration"] = (
            aws_sdk_compute_optimizer.types.volume_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "performanceRisk" in data:
        out["performance_risk"] = data["performanceRisk"]
    else:
        out["performance_risk"] = 0
    if "rank" in data:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if "savingsOpportunity" in data:
        import aws_sdk_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            aws_sdk_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if "savingsOpportunityAfterDiscounts" in data:
        import aws_sdk_compute_optimizer.types.ebs_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            aws_sdk_compute_optimizer.types.ebs_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    return out
