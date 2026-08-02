"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMetricDimensionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_dimension_result_set
    import capo_ec2.types.next_token


class GetCapacityManagerMetricDimensionsResult(TypedDict, closed=True):
    metric_dimension_results: NotRequired[
        "capo_ec2.types.metric_dimension_result_set.MetricDimensionResultSet"
    ]
    """<p> The available dimension combinations that have data within the specified time range and filters. </p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerMetricDimensionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_dimension_results" in value:
        import capo_ec2.types.metric_dimension_result_set

        capo_ec2.types.metric_dimension_result_set.serialize_ec2_query(
            value["metric_dimension_results"],
            pairs,
            f"{key_prefix}MetricDimensionResultSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetCapacityManagerMetricDimensionsResult:
    out: GetCapacityManagerMetricDimensionsResult = {}  # type: ignore[typeddict-item]
    if el.find("MetricDimensionResultSet") is not None:
        import capo_ec2.types.metric_dimension_result_set

        out["metric_dimension_results"] = (
            capo_ec2.types.metric_dimension_result_set.deserialize_ec2_query(
                el, "MetricDimensionResultSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
