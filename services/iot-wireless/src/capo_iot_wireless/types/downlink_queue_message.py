"""Generated from Smithy shape ``com.amazonaws.iotwireless#DownlinkQueueMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.iso_date_time_string
    import capo_iot_wireless.types.lo_ra_wan_send_data_to_device
    import capo_iot_wireless.types.message_id
    import capo_iot_wireless.types.transmit_mode


class DownlinkQueueMessage(TypedDict, closed=True):
    message_id: NotRequired["capo_iot_wireless.types.message_id.MessageId"]
    """<p> The message ID assigned by IoT Wireless to each downlink message, which helps identify the message.</p>"""
    transmit_mode: NotRequired["capo_iot_wireless.types.transmit_mode.TransmitMode"]
    """<p>The transmit mode to use for sending data to the wireless device. This can be <code>0</code> for UM (unacknowledge mode) or <code>1</code> for AM (acknowledge mode).</p>"""
    received_at: NotRequired[
        "capo_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The time at which Iot Wireless received the downlink message.</p>"""
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_send_data_to_device.LoRaWANSendDataToDevice"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkQueueMessage) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "transmit_mode" in value:
        out["TransmitMode"] = value["transmit_mode"]
    if "received_at" in value:
        out["ReceivedAt"] = value["received_at"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_send_data_to_device

        out["LoRaWAN"] = (
            capo_iot_wireless.types.lo_ra_wan_send_data_to_device.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> DownlinkQueueMessage:
    out: DownlinkQueueMessage = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    if "TransmitMode" in data:
        out["transmit_mode"] = data["TransmitMode"]
    if "ReceivedAt" in data:
        out["received_at"] = data["ReceivedAt"]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_send_data_to_device

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_send_data_to_device.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
