"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_gateway_id

WirelessGatewayList: TypeAlias = list[
    "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayList) -> list:
    return list(value)


def deserialize_json(data: list) -> WirelessGatewayList:
    return list(data)
