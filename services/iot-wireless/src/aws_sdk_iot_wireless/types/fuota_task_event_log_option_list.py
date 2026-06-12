"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskEventLogOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.fuota_task_event_log_option

FuotaTaskEventLogOptionList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.fuota_task_event_log_option.FuotaTaskEventLogOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaTaskEventLogOptionList) -> list:
    import aws_sdk_iot_wireless.types.fuota_task_event_log_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.fuota_task_event_log_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FuotaTaskEventLogOptionList:
    import aws_sdk_iot_wireless.types.fuota_task_event_log_option

    out: FuotaTaskEventLogOptionList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.fuota_task_event_log_option.deserialize_json(
                item
            )
        )
    return out
