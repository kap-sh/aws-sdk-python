"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBUtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.rdsdb_utilization_metric

RDSDBUtilizationMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.rdsdb_utilization_metric.RDSDBUtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBUtilizationMetrics) -> list:
    import aws_sdk_compute_optimizer.types.rdsdb_utilization_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.rdsdb_utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSDBUtilizationMetrics:
    import aws_sdk_compute_optimizer.types.rdsdb_utilization_metric

    out: RDSDBUtilizationMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.rdsdb_utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
