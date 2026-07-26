"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.enable_enhanced_metrics
    import capo_sagemaker.types.metric_publish_frequency_in_seconds


class MetricsConfig(TypedDict, closed=True):
    enable_enhanced_metrics: NotRequired[
        "capo_sagemaker.types.enable_enhanced_metrics.EnableEnhancedMetrics"
    ]
    """<p>Specifies whether to enable enhanced metrics for the endpoint. Enhanced metrics provide utilization and invocation data at instance and container granularity. Container granularity is supported for Inference Components. The default is <code>False</code>.</p>"""
    metric_publish_frequency_in_seconds: NotRequired[
        "capo_sagemaker.types.metric_publish_frequency_in_seconds.MetricPublishFrequencyInSeconds"
    ]
    """<p>The interval, in seconds, at which metrics are published to Amazon CloudWatch. Defaults to <code>60</code>. Valid values: <code>10</code>, <code>30</code>, <code>60</code>, <code>120</code>, <code>180</code>, <code>240</code>, <code>300</code>. When <code>EnableEnhancedMetrics</code> is set to <code>False</code>, this interval applies to utilization metrics only; invocation metrics continue to be published at the default 60-second interval. When <code>EnableEnhancedMetrics</code> is set to <code>True</code>, this interval applies to both utilization and invocation metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricsConfig) -> dict:
    out: dict = {}
    if "enable_enhanced_metrics" in value:
        out["EnableEnhancedMetrics"] = value["enable_enhanced_metrics"]
    if "metric_publish_frequency_in_seconds" in value:
        import capo_sagemaker.types.metric_publish_frequency_in_seconds

        out["MetricPublishFrequencyInSeconds"] = (
            capo_sagemaker.types.metric_publish_frequency_in_seconds.serialize_aws_json_1_1(
                value["metric_publish_frequency_in_seconds"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricsConfig:
    out: MetricsConfig = {}  # type: ignore[typeddict-item]
    if "EnableEnhancedMetrics" in data:
        out["enable_enhanced_metrics"] = data["EnableEnhancedMetrics"]
    if "MetricPublishFrequencyInSeconds" in data:
        import capo_sagemaker.types.metric_publish_frequency_in_seconds

        out["metric_publish_frequency_in_seconds"] = (
            capo_sagemaker.types.metric_publish_frequency_in_seconds.deserialize_aws_json_1_1(
                data["MetricPublishFrequencyInSeconds"]
            )
        )
    return out
