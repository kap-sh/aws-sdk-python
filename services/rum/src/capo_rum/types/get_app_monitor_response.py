"""Generated from Smithy shape ``com.amazonaws.rum#GetAppMonitorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.app_monitor


class GetAppMonitorResponse(TypedDict, closed=True):
    app_monitor: NotRequired["capo_rum.types.app_monitor.AppMonitor"]
    """<p>A structure containing all the configuration information for the app monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppMonitorResponse) -> dict:
    out: dict = {}
    if "app_monitor" in value:
        import capo_rum.types.app_monitor

        out["AppMonitor"] = capo_rum.types.app_monitor.serialize_json(
            value["app_monitor"]
        )
    return out


def deserialize_json(data: dict) -> GetAppMonitorResponse:
    out: GetAppMonitorResponse = {}  # type: ignore[typeddict-item]
    if "AppMonitor" in data:
        import capo_rum.types.app_monitor

        out["app_monitor"] = capo_rum.types.app_monitor.deserialize_json(
            data["AppMonitor"]
        )
    return out
