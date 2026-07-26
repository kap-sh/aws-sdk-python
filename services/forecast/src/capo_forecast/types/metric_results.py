"""Generated from Smithy shape ``com.amazonaws.forecast#MetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.metric_result

MetricResults: TypeAlias = list["capo_forecast.types.metric_result.MetricResult"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricResults) -> list:
    import capo_forecast.types.metric_result

    out: list = []
    for item in value:
        out.append(capo_forecast.types.metric_result.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricResults:
    import capo_forecast.types.metric_result

    out: MetricResults = []
    for item in data:
        out.append(capo_forecast.types.metric_result.deserialize_aws_json_1_1(item))
    return out
