"""Generated from Smithy shape ``com.amazonaws.machinelearning#PerformanceMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.performance_metrics_properties


class PerformanceMetrics(TypedDict, closed=True):
    properties: NotRequired[
        "capo_machine_learning.types.performance_metrics_properties.PerformanceMetricsProperties"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PerformanceMetrics) -> dict:
    out: dict = {}
    if "properties" in value:
        import capo_machine_learning.types.performance_metrics_properties

        out["Properties"] = (
            capo_machine_learning.types.performance_metrics_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PerformanceMetrics:
    out: PerformanceMetrics = {}  # type: ignore[typeddict-item]
    if "Properties" in data:
        import capo_machine_learning.types.performance_metrics_properties

        out["properties"] = (
            capo_machine_learning.types.performance_metrics_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
