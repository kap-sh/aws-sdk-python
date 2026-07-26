"""Generated from Smithy shape ``com.amazonaws.braket#DeviceQueueInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.device_queue_info

DeviceQueueInfoList: TypeAlias = list[
    "capo_braket.types.device_queue_info.DeviceQueueInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceQueueInfoList) -> list:
    import capo_braket.types.device_queue_info

    out: list = []
    for item in value:
        out.append(capo_braket.types.device_queue_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceQueueInfoList:
    import capo_braket.types.device_queue_info

    out: DeviceQueueInfoList = []
    for item in data:
        out.append(capo_braket.types.device_queue_info.deserialize_json(item))
    return out
