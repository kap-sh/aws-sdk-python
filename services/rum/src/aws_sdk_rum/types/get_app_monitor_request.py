"""Generated from Smithy shape ``com.amazonaws.rum#GetAppMonitorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_name


class GetAppMonitorRequest(TypedDict):
    name: "aws_sdk_rum.types.app_monitor_name.AppMonitorName"
    """<p>The app monitor to retrieve information for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppMonitorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAppMonitorRequest:
    out: GetAppMonitorRequest = {}  # type: ignore[typeddict-item]
    return out
