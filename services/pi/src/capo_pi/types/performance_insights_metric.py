"""Generated from Smithy shape ``com.amazonaws.pi#PerformanceInsightsMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.descriptive_map
    import capo_pi.types.descriptive_string
    import capo_pi.types.double


class PerformanceInsightsMetric(TypedDict, closed=True):
    metric: NotRequired["capo_pi.types.descriptive_string.DescriptiveString"]
    """<p>The Performance Insights metric.</p>"""
    display_name: NotRequired["capo_pi.types.descriptive_string.DescriptiveString"]
    """<p>The Performance Insights metric name.</p>"""
    dimensions: NotRequired["capo_pi.types.descriptive_map.DescriptiveMap"]
    """<p>A dimension map that contains the dimensions for this partition.</p>"""
    filter: NotRequired["capo_pi.types.descriptive_map.DescriptiveMap"]
    """<p>The filter for the Performance Insights metric.</p>"""
    value: NotRequired["capo_pi.types.double.Double"]
    """<p>The value of the metric. For example, <code>9</code> for <code>db.load.avg</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PerformanceInsightsMetric) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "dimensions" in value:
        import capo_pi.types.descriptive_map

        out["Dimensions"] = capo_pi.types.descriptive_map.serialize_aws_json_1_1(
            value["dimensions"]
        )
    if "filter" in value:
        import capo_pi.types.descriptive_map

        out["Filter"] = capo_pi.types.descriptive_map.serialize_aws_json_1_1(
            value["filter"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PerformanceInsightsMetric:
    out: PerformanceInsightsMetric = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        out["metric"] = data["Metric"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Dimensions" in data:
        import capo_pi.types.descriptive_map

        out["dimensions"] = capo_pi.types.descriptive_map.deserialize_aws_json_1_1(
            data["Dimensions"]
        )
    if "Filter" in data:
        import capo_pi.types.descriptive_map

        out["filter"] = capo_pi.types.descriptive_map.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
