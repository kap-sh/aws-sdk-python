"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchDashboardsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_summary_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class SearchDashboardsResponse(TypedDict):
    dashboard_summary_list: NotRequired[
        "aws_sdk_quicksight.types.dashboard_summary_list.DashboardSummaryList"
    ]
    """<p>The list of dashboards owned by the user specified in <code>Filters</code> in your request.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDashboardsResponse) -> dict:
    out: dict = {}
    if "dashboard_summary_list" in value:
        import aws_sdk_quicksight.types.dashboard_summary_list

        out["DashboardSummaryList"] = (
            aws_sdk_quicksight.types.dashboard_summary_list.serialize_json(
                value["dashboard_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchDashboardsResponse:
    out: SearchDashboardsResponse = {}  # type: ignore[typeddict-item]
    if "DashboardSummaryList" in data:
        import aws_sdk_quicksight.types.dashboard_summary_list

        out["dashboard_summary_list"] = (
            aws_sdk_quicksight.types.dashboard_summary_list.deserialize_json(
                data["DashboardSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
