"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task

FuotaTaskList: TypeAlias = list["capo_iot_wireless.types.fuota_task.FuotaTask"]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaTaskList) -> list:
    import capo_iot_wireless.types.fuota_task

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.fuota_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> FuotaTaskList:
    import capo_iot_wireless.types.fuota_task

    out: FuotaTaskList = []
    for item in data:
        out.append(capo_iot_wireless.types.fuota_task.deserialize_json(item))
    return out
