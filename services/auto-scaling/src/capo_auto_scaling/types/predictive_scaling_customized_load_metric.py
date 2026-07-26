"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredictiveScalingCustomizedLoadMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_data_queries


class PredictiveScalingCustomizedLoadMetric(TypedDict, closed=True):
    metric_data_queries: NotRequired[
        "capo_auto_scaling.types.metric_data_queries.MetricDataQueries"
    ]
    """<p>One or more metric data queries to provide the data points for a load metric. Use multiple metric data queries only if you are performing a math expression on returned data. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PredictiveScalingCustomizedLoadMetric,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "metric_data_queries" in value:
        import capo_auto_scaling.types.metric_data_queries

        capo_auto_scaling.types.metric_data_queries.serialize_query(
            value["metric_data_queries"], pairs, f"{prefix}.MetricDataQueries"
        )


def deserialize_query(el: Element) -> PredictiveScalingCustomizedLoadMetric:
    out: PredictiveScalingCustomizedLoadMetric = {}  # type: ignore[typeddict-item]
    child_metric_data_queries = el.find("MetricDataQueries")
    if child_metric_data_queries is not None:
        import capo_auto_scaling.types.metric_data_queries

        out["metric_data_queries"] = (
            capo_auto_scaling.types.metric_data_queries.deserialize_query(
                child_metric_data_queries
            )
        )
    return out
