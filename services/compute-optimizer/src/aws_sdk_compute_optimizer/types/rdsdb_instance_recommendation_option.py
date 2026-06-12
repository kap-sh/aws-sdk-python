"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBInstanceRecommendationOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.db_instance_class
    import aws_sdk_compute_optimizer.types.performance_risk
    import aws_sdk_compute_optimizer.types.rank
    import aws_sdk_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts
    import aws_sdk_compute_optimizer.types.rdsdb_projected_utilization_metrics
    import aws_sdk_compute_optimizer.types.savings_opportunity


class RDSDBInstanceRecommendationOption(TypedDict):
    db_instance_class: NotRequired[
        "aws_sdk_compute_optimizer.types.db_instance_class.DBInstanceClass"
    ]
    """<p> Describes the DB instance class recommendation option for your Amazon Aurora or RDS database. </p>"""
    projected_utilization_metrics: NotRequired[
        "aws_sdk_compute_optimizer.types.rdsdb_projected_utilization_metrics.RDSDBProjectedUtilizationMetrics"
    ]
    """<p> An array of objects that describe the projected utilization metrics of the DB instance recommendation option. </p>"""
    performance_risk: "aws_sdk_compute_optimizer.types.performance_risk.PerformanceRisk"
    """<p> The performance risk of the DB instance recommendation option. </p>"""
    rank: "aws_sdk_compute_optimizer.types.rank.Rank"
    """<p> The rank identifier of the DB instance recommendation option. </p>"""
    savings_opportunity: NotRequired[
        "aws_sdk_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    savings_opportunity_after_discounts: NotRequired[
        "aws_sdk_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts.RDSInstanceSavingsOpportunityAfterDiscounts"
    ]
    """<p> Describes the savings opportunity for Amazon Aurora and RDS database recommendations or for the recommendation option. </p> <p>Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBInstanceRecommendationOption) -> dict:
    out: dict = {}
    if "db_instance_class" in value:
        out["dbInstanceClass"] = value["db_instance_class"]
    if "projected_utilization_metrics" in value:
        import aws_sdk_compute_optimizer.types.rdsdb_projected_utilization_metrics

        out["projectedUtilizationMetrics"] = (
            aws_sdk_compute_optimizer.types.rdsdb_projected_utilization_metrics.serialize_aws_json_1_0(
                value["projected_utilization_metrics"]
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
        import aws_sdk_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            aws_sdk_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSDBInstanceRecommendationOption:
    out: RDSDBInstanceRecommendationOption = {}  # type: ignore[typeddict-item]
    if "dbInstanceClass" in data:
        out["db_instance_class"] = data["dbInstanceClass"]
    if "projectedUtilizationMetrics" in data:
        import aws_sdk_compute_optimizer.types.rdsdb_projected_utilization_metrics

        out["projected_utilization_metrics"] = (
            aws_sdk_compute_optimizer.types.rdsdb_projected_utilization_metrics.deserialize_aws_json_1_0(
                data["projectedUtilizationMetrics"]
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
        import aws_sdk_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            aws_sdk_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    return out
