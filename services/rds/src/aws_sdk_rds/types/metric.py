"""Generated from Smithy shape ``com.amazonaws.rds#Metric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.metric_query
    import aws_sdk_rds.types.metric_reference_list
    import aws_sdk_rds.types.string


class Metric(TypedDict, closed=True):
    name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of a metric.</p>"""
    references: NotRequired[
        "aws_sdk_rds.types.metric_reference_list.MetricReferenceList"
    ]
    """<p>A list of metric references (thresholds).</p>"""
    statistics_details: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The details of different statistics for a metric. The description might contain markdown.</p>"""
    metric_query: NotRequired["aws_sdk_rds.types.metric_query.MetricQuery"]
    """<p>The query to retrieve metric data points.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Metric, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "references" in value:
        import aws_sdk_rds.types.metric_reference_list

        aws_sdk_rds.types.metric_reference_list.serialize_query(
            value["references"], pairs, f"{prefix}.References"
        )
    if "statistics_details" in value:
        pairs.append((f"{prefix}.StatisticsDetails", str(value["statistics_details"])))
    if "metric_query" in value:
        import aws_sdk_rds.types.metric_query

        aws_sdk_rds.types.metric_query.serialize_query(
            value["metric_query"], pairs, f"{prefix}.MetricQuery"
        )


def deserialize_query(el: Element) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_references = el.find("References")
    if child_references is not None:
        import aws_sdk_rds.types.metric_reference_list

        out["references"] = aws_sdk_rds.types.metric_reference_list.deserialize_query(
            child_references
        )
    child_statistics_details = el.find("StatisticsDetails")
    if child_statistics_details is not None:
        out["statistics_details"] = str(child_statistics_details.text or "")
    child_metric_query = el.find("MetricQuery")
    if child_metric_query is not None:
        import aws_sdk_rds.types.metric_query

        out["metric_query"] = aws_sdk_rds.types.metric_query.deserialize_query(
            child_metric_query
        )
    return out
