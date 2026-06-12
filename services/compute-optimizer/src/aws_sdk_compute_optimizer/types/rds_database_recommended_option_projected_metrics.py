"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDatabaseRecommendedOptionProjectedMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.rds_database_recommended_option_projected_metric

RDSDatabaseRecommendedOptionProjectedMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.rds_database_recommended_option_projected_metric.RDSDatabaseRecommendedOptionProjectedMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDatabaseRecommendedOptionProjectedMetrics) -> list:
    import aws_sdk_compute_optimizer.types.rds_database_recommended_option_projected_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.rds_database_recommended_option_projected_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> RDSDatabaseRecommendedOptionProjectedMetrics:
    import aws_sdk_compute_optimizer.types.rds_database_recommended_option_projected_metric

    out: RDSDatabaseRecommendedOptionProjectedMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.rds_database_recommended_option_projected_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
