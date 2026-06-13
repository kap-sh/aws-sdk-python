"""Generated from Smithy shape ``com.amazonaws.amp#PrometheusMetricLabelMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amp.types.prometheus_metric_label_key
    import aws_sdk_amp.types.prometheus_metric_label_value

PrometheusMetricLabelMap: TypeAlias = dict[
    "aws_sdk_amp.types.prometheus_metric_label_key.PrometheusMetricLabelKey",
    "aws_sdk_amp.types.prometheus_metric_label_value.PrometheusMetricLabelValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PrometheusMetricLabelMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PrometheusMetricLabelMap:
    out: PrometheusMetricLabelMap = {}
    for key, value in data.items():
        out[key] = value
    return out
