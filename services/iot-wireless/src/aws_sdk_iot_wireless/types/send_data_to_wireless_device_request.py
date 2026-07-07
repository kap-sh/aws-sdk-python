"""Generated from Smithy shape ``com.amazonaws.iotwireless#SendDataToWirelessDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.payload_data
    import aws_sdk_iot_wireless.types.transmit_mode
    import aws_sdk_iot_wireless.types.wireless_device_id
    import aws_sdk_iot_wireless.types.wireless_metadata


class SendDataToWirelessDeviceRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of the wireless device to receive the data.</p>"""
    transmit_mode: "aws_sdk_iot_wireless.types.transmit_mode.TransmitMode"
    """<p>The transmit mode to use to send data to the wireless device. Can be: <code>0</code> for UM (unacknowledge mode) or <code>1</code> for AM (acknowledge mode).</p>"""
    payload_data: "aws_sdk_iot_wireless.types.payload_data.PayloadData"
    wireless_metadata: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_metadata.WirelessMetadata"
    ]
    """<p>Metadata about the message request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDataToWirelessDeviceRequest) -> dict:
    out: dict = {}
    out["TransmitMode"] = value["transmit_mode"]
    out["PayloadData"] = value["payload_data"]
    if "wireless_metadata" in value:
        import aws_sdk_iot_wireless.types.wireless_metadata

        out["WirelessMetadata"] = (
            aws_sdk_iot_wireless.types.wireless_metadata.serialize_json(
                value["wireless_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendDataToWirelessDeviceRequest:
    out: SendDataToWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
    if "TransmitMode" in data:
        out["transmit_mode"] = data["TransmitMode"]
    else:
        raise DeserializationError(
            "SendDataToWirelessDeviceRequest.transmit_mode required"
        )
    if "PayloadData" in data:
        out["payload_data"] = data["PayloadData"]
    else:
        raise DeserializationError(
            "SendDataToWirelessDeviceRequest.payload_data required"
        )
    if "WirelessMetadata" in data:
        import aws_sdk_iot_wireless.types.wireless_metadata

        out["wireless_metadata"] = (
            aws_sdk_iot_wireless.types.wireless_metadata.deserialize_json(
                data["WirelessMetadata"]
            )
        )
    return out
