"""Generated from Smithy shape ``com.amazonaws.iotwireless#MulticastGroupListByFuotaTask``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.multicast_group_by_fuota_task

MulticastGroupListByFuotaTask: TypeAlias = list[
    "aws_sdk_iot_wireless.types.multicast_group_by_fuota_task.MulticastGroupByFuotaTask"
]


# --- restJson1 ser/de ---
def serialize_json(value: MulticastGroupListByFuotaTask) -> list:
    import aws_sdk_iot_wireless.types.multicast_group_by_fuota_task

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.multicast_group_by_fuota_task.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MulticastGroupListByFuotaTask:
    import aws_sdk_iot_wireless.types.multicast_group_by_fuota_task

    out: MulticastGroupListByFuotaTask = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.multicast_group_by_fuota_task.deserialize_json(
                item
            )
        )
    return out
