"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayLogOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_gateway_log_option

WirelessGatewayLogOptionList: TypeAlias = list[
    "capo_iot_wireless.types.wireless_gateway_log_option.WirelessGatewayLogOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayLogOptionList) -> list:
    import capo_iot_wireless.types.wireless_gateway_log_option

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.wireless_gateway_log_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WirelessGatewayLogOptionList:
    import capo_iot_wireless.types.wireless_gateway_log_option

    out: WirelessGatewayLogOptionList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.wireless_gateway_log_option.deserialize_json(item)
        )
    return out
