"""Generated from Smithy shape ``com.amazonaws.rum#DeleteAppMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_name


class DeleteAppMonitorRequest(TypedDict, closed=True):
    name: "aws_sdk_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the app monitor to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppMonitorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAppMonitorRequest:
    out: DeleteAppMonitorRequest = {}  # type: ignore[typeddict-item]
    return out
