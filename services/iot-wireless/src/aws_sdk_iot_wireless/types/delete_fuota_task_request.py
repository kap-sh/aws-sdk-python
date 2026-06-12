"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteFuotaTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.fuota_task_id


class DeleteFuotaTaskRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.fuota_task_id.FuotaTaskId"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFuotaTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFuotaTaskRequest:
    out: DeleteFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    return out
