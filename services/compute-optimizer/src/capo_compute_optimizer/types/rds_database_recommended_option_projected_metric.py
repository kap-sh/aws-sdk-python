"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDatabaseRecommendedOptionProjectedMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.rank
    import capo_compute_optimizer.types.rds_database_projected_metrics
    import capo_compute_optimizer.types.recommended_db_instance_class


class RDSDatabaseRecommendedOptionProjectedMetric(TypedDict, closed=True):
    recommended_db_instance_class: NotRequired[
        "capo_compute_optimizer.types.recommended_db_instance_class.RecommendedDBInstanceClass"
    ]
    """<p> The recommended DB instance class for the Amazon Aurora or RDS database. </p>"""
    rank: "capo_compute_optimizer.types.rank.Rank"
    """<p> The rank identifier of the Amazon Aurora or RDS DB instance recommendation option. </p>"""
    projected_metrics: NotRequired[
        "capo_compute_optimizer.types.rds_database_projected_metrics.RDSDatabaseProjectedMetrics"
    ]
    """<p> An array of objects that describe the projected metric. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDatabaseRecommendedOptionProjectedMetric) -> dict:
    out: dict = {}
    if "recommended_db_instance_class" in value:
        out["recommendedDBInstanceClass"] = value["recommended_db_instance_class"]
    out["rank"] = value.get("rank", 0)
    if "projected_metrics" in value:
        import capo_compute_optimizer.types.rds_database_projected_metrics

        out["projectedMetrics"] = (
            capo_compute_optimizer.types.rds_database_projected_metrics.serialize_aws_json_1_0(
                value["projected_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSDatabaseRecommendedOptionProjectedMetric:
    out: RDSDatabaseRecommendedOptionProjectedMetric = {}  # type: ignore[typeddict-item]
    if "recommendedDBInstanceClass" in data:
        out["recommended_db_instance_class"] = data["recommendedDBInstanceClass"]
    if "rank" in data:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if "projectedMetrics" in data:
        import capo_compute_optimizer.types.rds_database_projected_metrics

        out["projected_metrics"] = (
            capo_compute_optimizer.types.rds_database_projected_metrics.deserialize_aws_json_1_0(
                data["projectedMetrics"]
            )
        )
    return out
