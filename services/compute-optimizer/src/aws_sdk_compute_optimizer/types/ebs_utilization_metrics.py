"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSUtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ebs_utilization_metric

EBSUtilizationMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.ebs_utilization_metric.EBSUtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSUtilizationMetrics) -> list:
    import aws_sdk_compute_optimizer.types.ebs_utilization_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.ebs_utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EBSUtilizationMetrics:
    import aws_sdk_compute_optimizer.types.ebs_utilization_metric

    out: EBSUtilizationMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.ebs_utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
