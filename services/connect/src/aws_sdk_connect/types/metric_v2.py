"""Generated from Smithy shape ``com.amazonaws.connect#MetricV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.metric_filters_v2_list
    import aws_sdk_connect.types.metric_id
    import aws_sdk_connect.types.metric_name_v2
    import aws_sdk_connect.types.threshold_collections


class MetricV2(TypedDict, closed=True):
    name: NotRequired["aws_sdk_connect.types.metric_name_v2.MetricNameV2"]
    """<p>The name of the metric.</p>"""
    threshold: NotRequired[
        "aws_sdk_connect.types.threshold_collections.ThresholdCollections"
    ]
    """<p>Contains information about the threshold for service level metrics.</p>"""
    metric_id: NotRequired["aws_sdk_connect.types.metric_id.MetricId"]
    """<p>Historical metrics or custom metrics can be referenced via this field. This field is a valid Connect Customer Arn or a UUID</p>"""
    metric_filters: NotRequired[
        "aws_sdk_connect.types.metric_filters_v2_list.MetricFiltersV2List"
    ]
    """<p>Contains the filters to be used when returning data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricV2) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "threshold" in value:
        import aws_sdk_connect.types.threshold_collections

        out["Threshold"] = aws_sdk_connect.types.threshold_collections.serialize_json(
            value["threshold"]
        )
    if "metric_id" in value:
        out["MetricId"] = value["metric_id"]
    if "metric_filters" in value:
        import aws_sdk_connect.types.metric_filters_v2_list

        out["MetricFilters"] = (
            aws_sdk_connect.types.metric_filters_v2_list.serialize_json(
                value["metric_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetricV2:
    out: MetricV2 = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Threshold" in data:
        import aws_sdk_connect.types.threshold_collections

        out["threshold"] = aws_sdk_connect.types.threshold_collections.deserialize_json(
            data["Threshold"]
        )
    if "MetricId" in data:
        out["metric_id"] = data["MetricId"]
    if "MetricFilters" in data:
        import aws_sdk_connect.types.metric_filters_v2_list

        out["metric_filters"] = (
            aws_sdk_connect.types.metric_filters_v2_list.deserialize_json(
                data["MetricFilters"]
            )
        )
    return out
