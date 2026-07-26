"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardPublishedVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class UpdateDashboardPublishedVersionResponse(TypedDict, closed=True):
    dashboard_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the dashboard.</p>"""
    dashboard_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dashboard.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardPublishedVersionResponse) -> dict:
    out: dict = {}
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateDashboardPublishedVersionResponse:
    out: UpdateDashboardPublishedVersionResponse = {}  # type: ignore[typeddict-item]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    if "DashboardArn" in data:
        out["dashboard_arn"] = data["DashboardArn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
