"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBStorageRecommendationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.db_storage_configuration
    import aws_sdk_compute_optimizer.types.rank
    import aws_sdk_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation
    import aws_sdk_compute_optimizer.types.rds_storage_savings_opportunity_after_discounts
    import aws_sdk_compute_optimizer.types.savings_opportunity


class RDSDBStorageRecommendationOption(TypedDict, closed=True):
    storage_configuration: NotRequired[
        "aws_sdk_compute_optimizer.types.db_storage_configuration.DBStorageConfiguration"
    ]
    """<p> The recommended storage configuration. </p>"""
    rank: "aws_sdk_compute_optimizer.types.rank.Rank"
    """<p> The rank identifier of the DB storage recommendation option. </p>"""
    savings_opportunity: NotRequired[
        "aws_sdk_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    savings_opportunity_after_discounts: NotRequired[
        "aws_sdk_compute_optimizer.types.rds_storage_savings_opportunity_after_discounts.RDSStorageSavingsOpportunityAfterDiscounts"
    ]
    """<p> Describes the savings opportunity for DB storage recommendations or for the recommendation option. </p> <p> Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation. </p>"""
    estimated_monthly_volume_io_ps_cost_variation: NotRequired[
        "aws_sdk_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation.RDSEstimatedMonthlyVolumeIOPsCostVariation"
    ]
    """<p> The projected level of variation in monthly I/O costs for the DB storage recommendation option. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBStorageRecommendationOption) -> dict:
    out: dict = {}
    if "storage_configuration" in value:
        import aws_sdk_compute_optimizer.types.db_storage_configuration

        out["storageConfiguration"] = (
            aws_sdk_compute_optimizer.types.db_storage_configuration.serialize_aws_json_1_0(
                value["storage_configuration"]
            )
        )
    out["rank"] = value.get("rank", 0)
    if "savings_opportunity" in value:
        import aws_sdk_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            aws_sdk_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import aws_sdk_compute_optimizer.types.rds_storage_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            aws_sdk_compute_optimizer.types.rds_storage_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    if "estimated_monthly_volume_io_ps_cost_variation" in value:
        import aws_sdk_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation

        out["estimatedMonthlyVolumeIOPsCostVariation"] = (
            aws_sdk_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation.serialize_aws_json_1_0(
                value["estimated_monthly_volume_io_ps_cost_variation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSDBStorageRecommendationOption:
    out: RDSDBStorageRecommendationOption = {}  # type: ignore[typeddict-item]
    if "storageConfiguration" in data:
        import aws_sdk_compute_optimizer.types.db_storage_configuration

        out["storage_configuration"] = (
            aws_sdk_compute_optimizer.types.db_storage_configuration.deserialize_aws_json_1_0(
                data["storageConfiguration"]
            )
        )
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
        import aws_sdk_compute_optimizer.types.rds_storage_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            aws_sdk_compute_optimizer.types.rds_storage_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    if "estimatedMonthlyVolumeIOPsCostVariation" in data:
        import aws_sdk_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation

        out["estimated_monthly_volume_io_ps_cost_variation"] = (
            aws_sdk_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation.deserialize_aws_json_1_0(
                data["estimatedMonthlyVolumeIOPsCostVariation"]
            )
        )
    return out
