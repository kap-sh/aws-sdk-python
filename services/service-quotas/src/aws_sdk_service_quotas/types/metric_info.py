"""Generated from Smithy shape ``com.amazonaws.servicequotas#MetricInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.metric_dimensions_map_definition
    import aws_sdk_service_quotas.types.quota_metric_name
    import aws_sdk_service_quotas.types.quota_metric_namespace
    import aws_sdk_service_quotas.types.statistic


class MetricInfo(TypedDict, closed=True):
    metric_namespace: NotRequired[
        "aws_sdk_service_quotas.types.quota_metric_namespace.QuotaMetricNamespace"
    ]
    """<p>The namespace of the metric.</p>"""
    metric_name: NotRequired[
        "aws_sdk_service_quotas.types.quota_metric_name.QuotaMetricName"
    ]
    """<p>The name of the metric.</p>"""
    metric_dimensions: NotRequired[
        "aws_sdk_service_quotas.types.metric_dimensions_map_definition.MetricDimensionsMapDefinition"
    ]
    """<p>The metric dimension. This is a name/value pair that is part of the identity of a metric.</p>"""
    metric_statistic_recommendation: NotRequired[
        "aws_sdk_service_quotas.types.statistic.Statistic"
    ]
    """<p>The metric statistic that we recommend you use when determining quota usage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricInfo) -> dict:
    out: dict = {}
    if "metric_namespace" in value:
        out["MetricNamespace"] = value["metric_namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "metric_dimensions" in value:
        import aws_sdk_service_quotas.types.metric_dimensions_map_definition

        out["MetricDimensions"] = (
            aws_sdk_service_quotas.types.metric_dimensions_map_definition.serialize_aws_json_1_1(
                value["metric_dimensions"]
            )
        )
    if "metric_statistic_recommendation" in value:
        out["MetricStatisticRecommendation"] = value["metric_statistic_recommendation"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricInfo:
    out: MetricInfo = {}  # type: ignore[typeddict-item]
    if "MetricNamespace" in data:
        out["metric_namespace"] = data["MetricNamespace"]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "MetricDimensions" in data:
        import aws_sdk_service_quotas.types.metric_dimensions_map_definition

        out["metric_dimensions"] = (
            aws_sdk_service_quotas.types.metric_dimensions_map_definition.deserialize_aws_json_1_1(
                data["MetricDimensions"]
            )
        )
    if "MetricStatisticRecommendation" in data:
        out["metric_statistic_recommendation"] = data["MetricStatisticRecommendation"]
    return out
