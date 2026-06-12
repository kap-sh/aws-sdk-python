"""Generated from Smithy shape ``com.amazonaws.pi#Data``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pi.types.performance_insights_metric


class Data(TypedDict):
    performance_insights_metric: NotRequired[
        "aws_sdk_pi.types.performance_insights_metric.PerformanceInsightsMetric"
    ]
    """<p>This field determines the Performance Insights metric to render for the insight. The <code>name</code> field refers to a Performance Insights metric. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Data) -> dict:
    out: dict = {}
    if "performance_insights_metric" in value:
        import aws_sdk_pi.types.performance_insights_metric

        out["PerformanceInsightsMetric"] = (
            aws_sdk_pi.types.performance_insights_metric.serialize_aws_json_1_1(
                value["performance_insights_metric"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Data:
    out: Data = {}  # type: ignore[typeddict-item]
    if "PerformanceInsightsMetric" in data:
        import aws_sdk_pi.types.performance_insights_metric

        out["performance_insights_metric"] = (
            aws_sdk_pi.types.performance_insights_metric.deserialize_aws_json_1_1(
                data["PerformanceInsightsMetric"]
            )
        )
    return out
