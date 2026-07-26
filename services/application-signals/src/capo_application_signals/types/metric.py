"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Metric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.dimensions
    import capo_application_signals.types.metric_name
    import capo_application_signals.types.namespace


class Metric(TypedDict, closed=True):
    namespace: NotRequired["capo_application_signals.types.namespace.Namespace"]
    r"""<p>The namespace of the metric. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace\">Namespaces</a>.</p>"""
    metric_name: NotRequired["capo_application_signals.types.metric_name.MetricName"]
    """<p>The name of the metric to use.</p>"""
    dimensions: NotRequired["capo_application_signals.types.dimensions.Dimensions"]
    r"""<p>An array of one or more dimensions to use to define the metric that you want to use. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension\">Dimensions</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Metric) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_application_signals.types.dimensions

        out["Dimensions"] = capo_application_signals.types.dimensions.serialize_json(
            value["dimensions"]
        )
    return out


def deserialize_json(data: dict) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Dimensions" in data:
        import capo_application_signals.types.dimensions

        out["dimensions"] = capo_application_signals.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    return out
