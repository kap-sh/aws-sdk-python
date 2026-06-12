"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayLogOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_log_option

WirelessGatewayLogOptionList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.wireless_gateway_log_option.WirelessGatewayLogOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayLogOptionList) -> list:
    import aws_sdk_iot_wireless.types.wireless_gateway_log_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.wireless_gateway_log_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WirelessGatewayLogOptionList:
    import aws_sdk_iot_wireless.types.wireless_gateway_log_option

    out: WirelessGatewayLogOptionList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.wireless_gateway_log_option.deserialize_json(
                item
            )
        )
    return out
