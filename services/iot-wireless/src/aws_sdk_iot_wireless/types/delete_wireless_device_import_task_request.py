"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteWirelessDeviceImportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.import_task_id


class DeleteWirelessDeviceImportTaskRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.import_task_id.ImportTaskId"
    """<p>The unique identifier of the import task to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWirelessDeviceImportTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWirelessDeviceImportTaskRequest:
    out: DeleteWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
    return out
