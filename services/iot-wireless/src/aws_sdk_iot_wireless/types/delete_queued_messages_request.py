"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteQueuedMessagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.message_id
    import aws_sdk_iot_wireless.types.wireless_device_id
    import aws_sdk_iot_wireless.types.wireless_device_type


class DeleteQueuedMessagesRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of a given wireless device for which downlink messages will be deleted.</p>"""
    message_id: "aws_sdk_iot_wireless.types.message_id.MessageId"
    """<p>If message ID is <code>\"*\"</code>, it cleares the entire downlink queue for a given device, specified by the wireless device ID. Otherwise, the downlink message with the specified message ID will be deleted.</p>"""
    wireless_device_type: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    ]
    """<p>The wireless device type, which can be either Sidewalk or LoRaWAN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueuedMessagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueuedMessagesRequest:
    out: DeleteQueuedMessagesRequest = {}  # type: ignore[typeddict-item]
    return out
