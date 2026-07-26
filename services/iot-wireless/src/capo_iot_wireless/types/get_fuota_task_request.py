"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetFuotaTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_id


class GetFuotaTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId"


# --- restJson1 ser/de ---
def serialize_json(value: GetFuotaTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFuotaTaskRequest:
    out: GetFuotaTaskRequest = {}  # type: ignore[typeddict-item]
    return out
