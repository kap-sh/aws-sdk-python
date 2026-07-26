"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMetricDataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_data_result_set
    import capo_ec2.types.next_token


class GetCapacityManagerMetricDataResult(TypedDict, closed=True):
    metric_data_results: NotRequired[
        "capo_ec2.types.metric_data_result_set.MetricDataResultSet"
    ]
    """<p> The metric data points returned by the query. Each result contains dimension values, timestamp, and metric values with their associated statistics. </p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerMetricDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "metric_data_results" in value:
        import capo_ec2.types.metric_data_result_set

        capo_ec2.types.metric_data_result_set.serialize_ec2_query(
            value["metric_data_results"], pairs, f"{prefix}.MetricDataResultSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetCapacityManagerMetricDataResult:
    out: GetCapacityManagerMetricDataResult = {}  # type: ignore[typeddict-item]
    if el.find("MetricDataResultSet") is not None:
        import capo_ec2.types.metric_data_result_set

        out["metric_data_results"] = (
            capo_ec2.types.metric_data_result_set.deserialize_ec2_query(
                el, "MetricDataResultSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
