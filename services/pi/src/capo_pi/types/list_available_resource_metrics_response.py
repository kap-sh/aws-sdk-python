"""Generated from Smithy shape ``com.amazonaws.pi#ListAvailableResourceMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.next_token
    import capo_pi.types.response_resource_metric_list


class ListAvailableResourceMetricsResponse(TypedDict, closed=True):
    metrics: NotRequired[
        "capo_pi.types.response_resource_metric_list.ResponseResourceMetricList"
    ]
    """<p>An array of metrics available to query. Each array element contains the full name, description, and unit of the metric. </p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>A pagination token that indicates the response didn’t return all available records because <code>MaxRecords</code> was specified in the previous request. To get the remaining records, specify <code>NextToken</code> in a separate request with this value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableResourceMetricsResponse) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_pi.types.response_resource_metric_list

        out["Metrics"] = (
            capo_pi.types.response_resource_metric_list.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableResourceMetricsResponse:
    out: ListAvailableResourceMetricsResponse = {}  # type: ignore[typeddict-item]
    if "Metrics" in data:
        import capo_pi.types.response_resource_metric_list

        out["metrics"] = (
            capo_pi.types.response_resource_metric_list.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
