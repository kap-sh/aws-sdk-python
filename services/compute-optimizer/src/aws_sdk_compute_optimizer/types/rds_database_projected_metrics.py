"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDatabaseProjectedMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.rds_database_projected_metric

RDSDatabaseProjectedMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.rds_database_projected_metric.RDSDatabaseProjectedMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDatabaseProjectedMetrics) -> list:
    import aws_sdk_compute_optimizer.types.rds_database_projected_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.rds_database_projected_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSDatabaseProjectedMetrics:
    import aws_sdk_compute_optimizer.types.rds_database_projected_metric

    out: RDSDatabaseProjectedMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.rds_database_projected_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
