"""Generated from Smithy shape ``com.amazonaws.iotwireless#GatewayListItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.downlink_frequency
    import aws_sdk_iot_wireless.types.wireless_gateway_id


class GatewayListItem(TypedDict):
    gateway_id: "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the wireless gateways that you want to add to the list of gateways when sending downlink messages.</p>"""
    downlink_frequency: (
        "aws_sdk_iot_wireless.types.downlink_frequency.DownlinkFrequency"
    )
    """<p>The frequency to use for the gateways when sending a downlink message to the wireless device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayListItem) -> dict:
    out: dict = {}
    out["GatewayId"] = value["gateway_id"]
    out["DownlinkFrequency"] = value["downlink_frequency"]
    return out


def deserialize_json(data: dict) -> GatewayListItem:
    out: GatewayListItem = {}  # type: ignore[typeddict-item]
    if "GatewayId" in data:
        out["gateway_id"] = data["GatewayId"]
    else:
        raise DeserializationError("GatewayListItem.gateway_id required")
    if "DownlinkFrequency" in data:
        out["downlink_frequency"] = data["DownlinkFrequency"]
    else:
        raise DeserializationError("GatewayListItem.downlink_frequency required")
    return out
