"""Generated from Smithy shape ``com.amazonaws.rum#GetAppMonitorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor


class GetAppMonitorResponse(TypedDict):
    app_monitor: NotRequired["aws_sdk_rum.types.app_monitor.AppMonitor"]
    """<p>A structure containing all the configuration information for the app monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppMonitorResponse) -> dict:
    out: dict = {}
    if "app_monitor" in value:
        import aws_sdk_rum.types.app_monitor

        out["AppMonitor"] = aws_sdk_rum.types.app_monitor.serialize_json(
            value["app_monitor"]
        )
    return out


def deserialize_json(data: dict) -> GetAppMonitorResponse:
    out: GetAppMonitorResponse = {}  # type: ignore[typeddict-item]
    if "AppMonitor" in data:
        import aws_sdk_rum.types.app_monitor

        out["app_monitor"] = aws_sdk_rum.types.app_monitor.deserialize_json(
            data["AppMonitor"]
        )
    return out
