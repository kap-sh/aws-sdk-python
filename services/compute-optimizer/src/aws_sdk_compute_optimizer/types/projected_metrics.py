"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ProjectedMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.projected_metric

ProjectedMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.projected_metric.ProjectedMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProjectedMetrics) -> list:
    import aws_sdk_compute_optimizer.types.projected_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.projected_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProjectedMetrics:
    import aws_sdk_compute_optimizer.types.projected_metric

    out: ProjectedMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.projected_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
