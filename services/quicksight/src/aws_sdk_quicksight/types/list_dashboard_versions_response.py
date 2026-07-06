"""Generated from Smithy shape ``com.amazonaws.quicksight#ListDashboardVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_version_summary_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListDashboardVersionsResponse(TypedDict, closed=True):
    dashboard_version_summary_list: NotRequired[
        "aws_sdk_quicksight.types.dashboard_version_summary_list.DashboardVersionSummaryList"
    ]
    """<p>A structure that contains information about each version of the dashboard.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDashboardVersionsResponse) -> dict:
    out: dict = {}
    if "dashboard_version_summary_list" in value:
        import aws_sdk_quicksight.types.dashboard_version_summary_list

        out["DashboardVersionSummaryList"] = (
            aws_sdk_quicksight.types.dashboard_version_summary_list.serialize_json(
                value["dashboard_version_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListDashboardVersionsResponse:
    out: ListDashboardVersionsResponse = {}  # type: ignore[typeddict-item]
    if "DashboardVersionSummaryList" in data:
        import aws_sdk_quicksight.types.dashboard_version_summary_list

        out["dashboard_version_summary_list"] = (
            aws_sdk_quicksight.types.dashboard_version_summary_list.deserialize_json(
                data["DashboardVersionSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
