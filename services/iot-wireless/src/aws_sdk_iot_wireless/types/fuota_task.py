"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTask``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.fuota_task_arn
    import aws_sdk_iot_wireless.types.fuota_task_id
    import aws_sdk_iot_wireless.types.fuota_task_name


class FuotaTask(TypedDict):
    id: NotRequired["aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId"]
    arn: NotRequired["aws_sdk_iot_wireless.types.fuota_task_arn.FuotaTaskArn"]
    name: NotRequired["aws_sdk_iot_wireless.types.fuota_task_name.FuotaTaskName"]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaTask) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> FuotaTask:
    out: FuotaTask = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
