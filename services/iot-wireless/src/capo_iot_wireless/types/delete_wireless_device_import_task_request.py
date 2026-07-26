"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteWirelessDeviceImportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.import_task_id


class DeleteWirelessDeviceImportTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.import_task_id.ImportTaskId"
    """<p>The unique identifier of the import task to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWirelessDeviceImportTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWirelessDeviceImportTaskRequest:
    out: DeleteWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
    return out
