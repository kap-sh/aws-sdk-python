"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskLogOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_log_option

FuotaTaskLogOptionList: TypeAlias = list[
    "capo_iot_wireless.types.fuota_task_log_option.FuotaTaskLogOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaTaskLogOptionList) -> list:
    import capo_iot_wireless.types.fuota_task_log_option

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.fuota_task_log_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> FuotaTaskLogOptionList:
    import capo_iot_wireless.types.fuota_task_log_option

    out: FuotaTaskLogOptionList = []
    for item in data:
        out.append(capo_iot_wireless.types.fuota_task_log_option.deserialize_json(item))
    return out
