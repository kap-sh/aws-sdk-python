"""Generated from Smithy shape ``com.amazonaws.quicksight#ListDashboardsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_summary_list
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class ListDashboardsResponse(TypedDict, closed=True):
    dashboard_summary_list: NotRequired[
        "capo_quicksight.types.dashboard_summary_list.DashboardSummaryList"
    ]
    """<p>A structure that contains all of the dashboards in your Amazon Web Services account. This structure provides basic information about the dashboards.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDashboardsResponse) -> dict:
    out: dict = {}
    if "dashboard_summary_list" in value:
        import capo_quicksight.types.dashboard_summary_list

        out["DashboardSummaryList"] = (
            capo_quicksight.types.dashboard_summary_list.serialize_json(
                value["dashboard_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListDashboardsResponse:
    out: ListDashboardsResponse = {}  # type: ignore[typeddict-item]
    if "DashboardSummaryList" in data:
        import capo_quicksight.types.dashboard_summary_list

        out["dashboard_summary_list"] = (
            capo_quicksight.types.dashboard_summary_list.deserialize_json(
                data["DashboardSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
