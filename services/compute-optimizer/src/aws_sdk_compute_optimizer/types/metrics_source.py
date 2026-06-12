"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricsSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.metric_source

MetricsSource: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.metric_source.MetricSource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricsSource) -> list:
    import aws_sdk_compute_optimizer.types.metric_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.metric_source.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MetricsSource:
    import aws_sdk_compute_optimizer.types.metric_source

    out: MetricsSource = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.metric_source.deserialize_aws_json_1_0(item)
        )
    return out
