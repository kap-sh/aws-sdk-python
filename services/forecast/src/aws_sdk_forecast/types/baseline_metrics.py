"""Generated from Smithy shape ``com.amazonaws.forecast#BaselineMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.baseline_metric

BaselineMetrics: TypeAlias = list[
    "aws_sdk_forecast.types.baseline_metric.BaselineMetric"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BaselineMetrics) -> list:
    import aws_sdk_forecast.types.baseline_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_forecast.types.baseline_metric.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BaselineMetrics:
    import aws_sdk_forecast.types.baseline_metric

    out: BaselineMetrics = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.baseline_metric.deserialize_aws_json_1_1(item)
        )
    return out
