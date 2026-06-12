"""Generated from Smithy shape ``com.amazonaws.rum#ListAppMonitorsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_summary_list

class ListAppMonitorsResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p>A token that you can use in a subsequent operation to retrieve the next set of results.</p>"""
    app_monitor_summaries: NotRequired["aws_sdk_rum.types.app_monitor_summary_list.AppMonitorSummaryList"]
    """<p>An array of structures that contain information about the returned app monitors.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListAppMonitorsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "app_monitor_summaries" in value:
        import aws_sdk_rum.types.app_monitor_summary_list
        out["AppMonitorSummaries"] = aws_sdk_rum.types.app_monitor_summary_list.serialize_json(value["app_monitor_summaries"])
    return out


def deserialize_json(data: dict) -> ListAppMonitorsResponse:
    out: ListAppMonitorsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AppMonitorSummaries" in data:
        import aws_sdk_rum.types.app_monitor_summary_list
        out["app_monitor_summaries"] = aws_sdk_rum.types.app_monitor_summary_list.deserialize_json(data["AppMonitorSummaries"])
    return out