"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_send_data_to_device
    import aws_sdk_iot_wireless.types.sidewalk_send_data_to_device


class WirelessMetadata(TypedDict, closed=True):
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_send_data_to_device.LoRaWANSendDataToDevice"
    ]
    """<p>LoRaWAN device info.</p>"""
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_send_data_to_device.SidewalkSendDataToDevice"
    ]
    """<p>The Sidewalk account credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WirelessMetadata) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_send_data_to_device

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_send_data_to_device.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_send_data_to_device

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_send_data_to_device.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> WirelessMetadata:
    out: WirelessMetadata = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_send_data_to_device

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_send_data_to_device.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_send_data_to_device

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_send_data_to_device.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
