"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_gateway_statistics

WirelessGatewayStatisticsList: TypeAlias = list[
    "capo_iot_wireless.types.wireless_gateway_statistics.WirelessGatewayStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayStatisticsList) -> list:
    import capo_iot_wireless.types.wireless_gateway_statistics

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.wireless_gateway_statistics.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WirelessGatewayStatisticsList:
    import capo_iot_wireless.types.wireless_gateway_statistics

    out: WirelessGatewayStatisticsList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.wireless_gateway_statistics.deserialize_json(item)
        )
    return out
