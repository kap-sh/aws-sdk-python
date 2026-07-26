"""Generated from Smithy shape ``com.amazonaws.forecast#ErrorMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.error_metric

ErrorMetrics: TypeAlias = list["capo_forecast.types.error_metric.ErrorMetric"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorMetrics) -> list:
    import capo_forecast.types.error_metric

    out: list = []
    for item in value:
        out.append(capo_forecast.types.error_metric.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ErrorMetrics:
    import capo_forecast.types.error_metric

    out: ErrorMetrics = []
    for item in data:
        out.append(capo_forecast.types.error_metric.deserialize_aws_json_1_1(item))
    return out
