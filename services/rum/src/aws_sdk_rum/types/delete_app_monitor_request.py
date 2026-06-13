"""Generated from Smithy shape ``com.amazonaws.rum#DeleteAppMonitorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_name


class DeleteAppMonitorRequest(TypedDict):
    name: "aws_sdk_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the app monitor to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppMonitorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppMonitorRequest:
    out: DeleteAppMonitorRequest = {}  # type: ignore[typeddict-item]
    return out
