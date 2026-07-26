"""Generated from Smithy shape ``com.amazonaws.iotwireless#StartSingleWirelessDeviceImportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.import_task_arn
    import capo_iot_wireless.types.import_task_id


class StartSingleWirelessDeviceImportTaskResponse(TypedDict, closed=True):
    id: NotRequired["capo_iot_wireless.types.import_task_id.ImportTaskId"]
    """<p>The import task ID.</p>"""
    arn: NotRequired["capo_iot_wireless.types.import_task_arn.ImportTaskArn"]
    """<p>The ARN (Amazon Resource Name) of the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSingleWirelessDeviceImportTaskResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StartSingleWirelessDeviceImportTaskResponse:
    out: StartSingleWirelessDeviceImportTaskResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
