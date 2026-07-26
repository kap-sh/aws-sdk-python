"""Generated from Smithy shape ``com.amazonaws.machinelearning#PerformanceMetricsProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_machine_learning.types.performance_metrics_property_key
    import capo_machine_learning.types.performance_metrics_property_value

PerformanceMetricsProperties: TypeAlias = dict[
    "capo_machine_learning.types.performance_metrics_property_key.PerformanceMetricsPropertyKey",
    "capo_machine_learning.types.performance_metrics_property_value.PerformanceMetricsPropertyValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PerformanceMetricsProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> PerformanceMetricsProperties:
    out: PerformanceMetricsProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
