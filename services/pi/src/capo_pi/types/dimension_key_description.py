"""Generated from Smithy shape ``com.amazonaws.pi#DimensionKeyDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.additional_metrics_map
    import capo_pi.types.dimension_map
    import capo_pi.types.double
    import capo_pi.types.metric_values_list


class DimensionKeyDescription(TypedDict, closed=True):
    dimensions: NotRequired["capo_pi.types.dimension_map.DimensionMap"]
    """<p>A map of name-value pairs for the dimensions in the group.</p>"""
    total: NotRequired["capo_pi.types.double.Double"]
    """<p>The aggregated metric value for the dimensions, over the requested time range.</p>"""
    additional_metrics: NotRequired[
        "capo_pi.types.additional_metrics_map.AdditionalMetricsMap"
    ]
    """<p>A map that contains the value for each additional metric.</p>"""
    partitions: NotRequired["capo_pi.types.metric_values_list.MetricValuesList"]
    """<p>If <code>PartitionBy</code> was specified, <code>PartitionKeys</code> contains the dimensions that were.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionKeyDescription) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_pi.types.dimension_map

        out["Dimensions"] = capo_pi.types.dimension_map.serialize_aws_json_1_1(
            value["dimensions"]
        )
    if "total" in value:
        out["Total"] = value["total"]
    if "additional_metrics" in value:
        import capo_pi.types.additional_metrics_map

        out["AdditionalMetrics"] = (
            capo_pi.types.additional_metrics_map.serialize_aws_json_1_1(
                value["additional_metrics"]
            )
        )
    if "partitions" in value:
        import capo_pi.types.metric_values_list

        out["Partitions"] = capo_pi.types.metric_values_list.serialize_aws_json_1_1(
            value["partitions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DimensionKeyDescription:
    out: DimensionKeyDescription = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import capo_pi.types.dimension_map

        out["dimensions"] = capo_pi.types.dimension_map.deserialize_aws_json_1_1(
            data["Dimensions"]
        )
    if "Total" in data:
        out["total"] = data["Total"]
    if "AdditionalMetrics" in data:
        import capo_pi.types.additional_metrics_map

        out["additional_metrics"] = (
            capo_pi.types.additional_metrics_map.deserialize_aws_json_1_1(
                data["AdditionalMetrics"]
            )
        )
    if "Partitions" in data:
        import capo_pi.types.metric_values_list

        out["partitions"] = capo_pi.types.metric_values_list.deserialize_aws_json_1_1(
            data["Partitions"]
        )
    return out
