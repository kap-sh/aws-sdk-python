"""Generated from Smithy shape ``com.amazonaws.rds#MetricQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.performance_insights_metric_query


class MetricQuery(TypedDict, closed=True):
    performance_insights_metric_query: NotRequired[
        "capo_rds.types.performance_insights_metric_query.PerformanceInsightsMetricQuery"
    ]
    """<p>The Performance Insights query that you can use to retrieve Performance Insights metric data points.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "performance_insights_metric_query" in value:
        import capo_rds.types.performance_insights_metric_query

        capo_rds.types.performance_insights_metric_query.serialize_query(
            value["performance_insights_metric_query"],
            pairs,
            f"{key_prefix}PerformanceInsightsMetricQuery",
        )


def deserialize_query(el: Element) -> MetricQuery:
    out: MetricQuery = {}  # type: ignore[typeddict-item]
    child_performance_insights_metric_query = el.find("PerformanceInsightsMetricQuery")
    if child_performance_insights_metric_query is not None:
        import capo_rds.types.performance_insights_metric_query

        out["performance_insights_metric_query"] = (
            capo_rds.types.performance_insights_metric_query.deserialize_query(
                child_performance_insights_metric_query
            )
        )
    return out
