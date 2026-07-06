"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeMetricCollectionTypesAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.metric_collection_types
    import aws_sdk_auto_scaling.types.metric_granularity_types


class DescribeMetricCollectionTypesAnswer(TypedDict, closed=True):
    metrics: NotRequired[
        "aws_sdk_auto_scaling.types.metric_collection_types.MetricCollectionTypes"
    ]
    """<p>The metrics.</p>"""
    granularities: NotRequired[
        "aws_sdk_auto_scaling.types.metric_granularity_types.MetricGranularityTypes"
    ]
    """<p>The granularities for the metrics.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeMetricCollectionTypesAnswer,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "metrics" in value:
        import aws_sdk_auto_scaling.types.metric_collection_types

        aws_sdk_auto_scaling.types.metric_collection_types.serialize_query(
            value["metrics"], pairs, f"{prefix}.Metrics"
        )
    if "granularities" in value:
        import aws_sdk_auto_scaling.types.metric_granularity_types

        aws_sdk_auto_scaling.types.metric_granularity_types.serialize_query(
            value["granularities"], pairs, f"{prefix}.Granularities"
        )


def deserialize_query(el: Element) -> DescribeMetricCollectionTypesAnswer:
    out: DescribeMetricCollectionTypesAnswer = {}  # type: ignore[typeddict-item]
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import aws_sdk_auto_scaling.types.metric_collection_types

        out["metrics"] = (
            aws_sdk_auto_scaling.types.metric_collection_types.deserialize_query(
                child_metrics
            )
        )
    child_granularities = el.find("Granularities")
    if child_granularities is not None:
        import aws_sdk_auto_scaling.types.metric_granularity_types

        out["granularities"] = (
            aws_sdk_auto_scaling.types.metric_granularity_types.deserialize_query(
                child_granularities
            )
        )
    return out
