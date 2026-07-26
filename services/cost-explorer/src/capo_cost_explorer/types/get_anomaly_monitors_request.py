"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetAnomalyMonitorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.page_size
    import capo_cost_explorer.types.values


class GetAnomalyMonitorsRequest(TypedDict, closed=True):
    monitor_arn_list: NotRequired["capo_cost_explorer.types.values.Values"]
    """<p>A list of cost anomaly monitor ARNs. </p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""
    max_results: NotRequired["capo_cost_explorer.types.page_size.PageSize"]
    """<p>The number of entries that a paginated response contains. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAnomalyMonitorsRequest) -> dict:
    out: dict = {}
    if "monitor_arn_list" in value:
        import capo_cost_explorer.types.values

        out["MonitorArnList"] = capo_cost_explorer.types.values.serialize_aws_json_1_1(
            value["monitor_arn_list"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAnomalyMonitorsRequest:
    out: GetAnomalyMonitorsRequest = {}  # type: ignore[typeddict-item]
    if "MonitorArnList" in data:
        import capo_cost_explorer.types.values

        out["monitor_arn_list"] = (
            capo_cost_explorer.types.values.deserialize_aws_json_1_1(
                data["MonitorArnList"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
