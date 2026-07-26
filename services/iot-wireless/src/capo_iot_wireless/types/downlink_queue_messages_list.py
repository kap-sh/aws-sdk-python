"""Generated from Smithy shape ``com.amazonaws.iotwireless#DownlinkQueueMessagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.downlink_queue_message

DownlinkQueueMessagesList: TypeAlias = list[
    "capo_iot_wireless.types.downlink_queue_message.DownlinkQueueMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkQueueMessagesList) -> list:
    import capo_iot_wireless.types.downlink_queue_message

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.downlink_queue_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> DownlinkQueueMessagesList:
    import capo_iot_wireless.types.downlink_queue_message

    out: DownlinkQueueMessagesList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.downlink_queue_message.deserialize_json(item)
        )
    return out
