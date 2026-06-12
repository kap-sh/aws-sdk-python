"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBProjectedUtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.rdsdb_utilization_metric

RDSDBProjectedUtilizationMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.rdsdb_utilization_metric.RDSDBUtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBProjectedUtilizationMetrics) -> list:
    import aws_sdk_compute_optimizer.types.rdsdb_utilization_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.rdsdb_utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSDBProjectedUtilizationMetrics:
    import aws_sdk_compute_optimizer.types.rdsdb_utilization_metric

    out: RDSDBProjectedUtilizationMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.rdsdb_utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
