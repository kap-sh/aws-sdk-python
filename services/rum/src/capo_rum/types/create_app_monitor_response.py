"""Generated from Smithy shape ``com.amazonaws.rum#CreateAppMonitorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_id


class CreateAppMonitorResponse(TypedDict, closed=True):
    id: NotRequired["capo_rum.types.app_monitor_id.AppMonitorId"]
    """<p>The unique ID of the new app monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppMonitorResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateAppMonitorResponse:
    out: CreateAppMonitorResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
