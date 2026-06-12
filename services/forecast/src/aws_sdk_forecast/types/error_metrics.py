"""Generated from Smithy shape ``com.amazonaws.forecast#ErrorMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.error_metric

ErrorMetrics: TypeAlias = list["aws_sdk_forecast.types.error_metric.ErrorMetric"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorMetrics) -> list:
    import aws_sdk_forecast.types.error_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_forecast.types.error_metric.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ErrorMetrics:
    import aws_sdk_forecast.types.error_metric

    out: ErrorMetrics = []
    for item in data:
        out.append(aws_sdk_forecast.types.error_metric.deserialize_aws_json_1_1(item))
    return out
