"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessDeviceImportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.import_task_id


class GetWirelessDeviceImportTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.import_task_id.ImportTaskId"
    """<p>The identifier of the import task for which information is requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessDeviceImportTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWirelessDeviceImportTaskRequest:
    out: GetWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
    return out
