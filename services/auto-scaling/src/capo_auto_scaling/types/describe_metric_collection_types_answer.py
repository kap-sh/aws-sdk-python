"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeMetricCollectionTypesAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_collection_types
    import capo_auto_scaling.types.metric_granularity_types


class DescribeMetricCollectionTypesAnswer(TypedDict, closed=True):
    metrics: NotRequired[
        "capo_auto_scaling.types.metric_collection_types.MetricCollectionTypes"
    ]
    """<p>The metrics.</p>"""
    granularities: NotRequired[
        "capo_auto_scaling.types.metric_granularity_types.MetricGranularityTypes"
    ]
    """<p>The granularities for the metrics.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeMetricCollectionTypesAnswer,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metrics" in value:
        import capo_auto_scaling.types.metric_collection_types

        capo_auto_scaling.types.metric_collection_types.serialize_query(
            value["metrics"], pairs, f"{key_prefix}Metrics"
        )
    if "granularities" in value:
        import capo_auto_scaling.types.metric_granularity_types

        capo_auto_scaling.types.metric_granularity_types.serialize_query(
            value["granularities"], pairs, f"{key_prefix}Granularities"
        )


def deserialize_query(el: Element) -> DescribeMetricCollectionTypesAnswer:
    out: DescribeMetricCollectionTypesAnswer = {}  # type: ignore[typeddict-item]
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import capo_auto_scaling.types.metric_collection_types

        out["metrics"] = (
            capo_auto_scaling.types.metric_collection_types.deserialize_query(
                child_metrics
            )
        )
    child_granularities = el.find("Granularities")
    if child_granularities is not None:
        import capo_auto_scaling.types.metric_granularity_types

        out["granularities"] = (
            capo_auto_scaling.types.metric_granularity_types.deserialize_query(
                child_granularities
            )
        )
    return out
