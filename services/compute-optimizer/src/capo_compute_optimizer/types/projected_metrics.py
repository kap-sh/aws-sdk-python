"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ProjectedMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.projected_metric

ProjectedMetrics: TypeAlias = list[
    "capo_compute_optimizer.types.projected_metric.ProjectedMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProjectedMetrics) -> list:
    import capo_compute_optimizer.types.projected_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.projected_metric.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProjectedMetrics:
    import capo_compute_optimizer.types.projected_metric

    out: ProjectedMetrics = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.projected_metric.deserialize_aws_json_1_0(item)
        )
    return out
