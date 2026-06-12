"""Generated from Smithy shape ``com.amazonaws.iotwireless#StartWirelessDeviceImportTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.import_task_arn
    import aws_sdk_iot_wireless.types.import_task_id


class StartWirelessDeviceImportTaskResponse(TypedDict):
    id: NotRequired["aws_sdk_iot_wireless.types.import_task_id.ImportTaskId"]
    """<p>The import task ID.</p>"""
    arn: NotRequired["aws_sdk_iot_wireless.types.import_task_arn.ImportTaskArn"]
    """<p>The ARN (Amazon Resource Name) of the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartWirelessDeviceImportTaskResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StartWirelessDeviceImportTaskResponse:
    out: StartWirelessDeviceImportTaskResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
