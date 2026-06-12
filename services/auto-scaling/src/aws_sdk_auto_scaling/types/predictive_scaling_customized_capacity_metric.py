"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredictiveScalingCustomizedCapacityMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.metric_data_queries


class PredictiveScalingCustomizedCapacityMetric(TypedDict):
    metric_data_queries: NotRequired[
        "aws_sdk_auto_scaling.types.metric_data_queries.MetricDataQueries"
    ]
    """<p>One or more metric data queries to provide the data points for a capacity metric. Use multiple metric data queries only if you are performing a math expression on returned data. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PredictiveScalingCustomizedCapacityMetric,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "metric_data_queries" in value:
        import aws_sdk_auto_scaling.types.metric_data_queries

        aws_sdk_auto_scaling.types.metric_data_queries.serialize_query(
            value["metric_data_queries"], pairs, f"{prefix}.MetricDataQueries"
        )


def deserialize_query(el: Element) -> PredictiveScalingCustomizedCapacityMetric:
    out: PredictiveScalingCustomizedCapacityMetric = {}  # type: ignore[typeddict-item]
    child_metric_data_queries = el.find("MetricDataQueries")
    if child_metric_data_queries is not None:
        import aws_sdk_auto_scaling.types.metric_data_queries

        out["metric_data_queries"] = (
            aws_sdk_auto_scaling.types.metric_data_queries.deserialize_query(
                child_metric_data_queries
            )
        )
    return out
