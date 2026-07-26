"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardVisualResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_name
    import capo_quicksight.types.qa_url
    import capo_quicksight.types.sheet_name
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.visual_subtitle
    import capo_quicksight.types.visual_title


class DashboardVisualResult(TypedDict, closed=True):
    dashboard_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the dashboard.</p>"""
    dashboard_name: NotRequired["capo_quicksight.types.dashboard_name.DashboardName"]
    """<p>The name of the dashboard.</p>"""
    sheet_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the sheet.</p>"""
    sheet_name: NotRequired["capo_quicksight.types.sheet_name.SheetName"]
    """<p>The name of the sheet.</p>"""
    visual_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the visual.</p>"""
    visual_title: NotRequired["capo_quicksight.types.visual_title.VisualTitle"]
    """<p>The title of the visual.</p>"""
    visual_subtitle: NotRequired["capo_quicksight.types.visual_subtitle.VisualSubtitle"]
    """<p>The subtitle of the visual.</p>"""
    dashboard_url: NotRequired["capo_quicksight.types.qa_url.QAUrl"]
    """<p>The URL of the dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardVisualResult) -> dict:
    out: dict = {}
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "dashboard_name" in value:
        out["DashboardName"] = value["dashboard_name"]
    if "sheet_id" in value:
        out["SheetId"] = value["sheet_id"]
    if "sheet_name" in value:
        out["SheetName"] = value["sheet_name"]
    if "visual_id" in value:
        out["VisualId"] = value["visual_id"]
    if "visual_title" in value:
        out["VisualTitle"] = value["visual_title"]
    if "visual_subtitle" in value:
        out["VisualSubtitle"] = value["visual_subtitle"]
    if "dashboard_url" in value:
        out["DashboardUrl"] = value["dashboard_url"]
    return out


def deserialize_json(data: dict) -> DashboardVisualResult:
    out: DashboardVisualResult = {}  # type: ignore[typeddict-item]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    if "DashboardName" in data:
        out["dashboard_name"] = data["DashboardName"]
    if "SheetId" in data:
        out["sheet_id"] = data["SheetId"]
    if "SheetName" in data:
        out["sheet_name"] = data["SheetName"]
    if "VisualId" in data:
        out["visual_id"] = data["VisualId"]
    if "VisualTitle" in data:
        out["visual_title"] = data["VisualTitle"]
    if "VisualSubtitle" in data:
        out["visual_subtitle"] = data["VisualSubtitle"]
    if "DashboardUrl" in data:
        out["dashboard_url"] = data["DashboardUrl"]
    return out
