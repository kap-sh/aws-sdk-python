"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateFuotaTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.fuota_task_arn
    import aws_sdk_iot_wireless.types.fuota_task_id


class CreateFuotaTaskResponse(TypedDict):
    arn: NotRequired["aws_sdk_iot_wireless.types.fuota_task_arn.FuotaTaskArn"]
    id: NotRequired["aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateFuotaTaskResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateFuotaTaskResponse:
    out: CreateFuotaTaskResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
