"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardVisualId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DashboardVisualId(TypedDict, closed=True):
    dashboard_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the dashboard that has the visual that you want to embed. The <code>DashboardId</code> can be found in the <code>IDs for developers</code> section of the <code>Embed visual</code> pane of the visual's on-visual menu of the Quick console. You can also get the <code>DashboardId</code> with a <code>ListDashboards</code> API operation.</p>"""
    sheet_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the sheet that the has visual that you want to embed. The <code>SheetId</code> can be found in the <code>IDs for developers</code> section of the <code>Embed visual</code> pane of the visual's on-visual menu of the Quick console.</p>"""
    visual_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the visual that you want to embed. The <code>VisualID</code> can be found in the <code>IDs for developers</code> section of the <code>Embed visual</code> pane of the visual's on-visual menu of the Amazon Quick Sight console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardVisualId) -> dict:
    out: dict = {}
    out["DashboardId"] = value["dashboard_id"]
    out["SheetId"] = value["sheet_id"]
    out["VisualId"] = value["visual_id"]
    return out


def deserialize_json(data: dict) -> DashboardVisualId:
    out: DashboardVisualId = {}  # type: ignore[typeddict-item]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    else:
        raise DeserializationError("DashboardVisualId.dashboard_id required")
    if "SheetId" in data:
        out["sheet_id"] = data["SheetId"]
    else:
        raise DeserializationError("DashboardVisualId.sheet_id required")
    if "VisualId" in data:
        out["visual_id"] = data["VisualId"]
    else:
        raise DeserializationError("DashboardVisualId.visual_id required")
    return out
